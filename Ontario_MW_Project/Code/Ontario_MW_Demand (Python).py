# %%
import pandas as pd
import glob
import datetime
import matplotlib.pyplot as plt
import xgboost as xgb
import numpy as np
from sklearn.metrics import root_mean_squared_error
from xgboost import plot_importance

# %% [markdown]
# IMPORTING/ CLEANING DATA

# %%
#import 2015 to 2025 MW demand data, ignore title row from each and concatenate all csv files together by row, adding new title row
path = "IESO_MW_Data"
all_files = glob.glob(path + "/*.csv")
dfs = []
for files in all_files:
    df_2 = pd.read_csv(files, skiprows=1, header=None)
    df_2.columns = ["Datetime", "Hour", "Market Demand", "Ontario Demand"]
    dfs.append(df_2)
df = pd.concat(dfs, ignore_index=True, axis=0)

# %%

#Set hour to numeric, replace hour 24 with hour 0 for easier datetime conversion
df['Hour']=pd.to_numeric(df['Hour'], errors='coerce')
df['Hour'] = df['Hour'].replace(24,0)


#Convert Date column to datetime format, combine with hour column, drop hour column
df['Datetime'] = pd.to_datetime(df["Datetime"], format="%Y-%m-%d")
df["Datetime"] = df["Datetime"] + pd.to_timedelta(df['Hour'], unit='h')
df = df.set_index('Datetime')
df.drop(columns=['Hour'], inplace=True)
df.drop(columns=['Market Demand'], inplace=True)
df

# %%
#Separate train and test sets (trial: 70/30 split)

#Determine number of unique hours in Datetime index, calculate 70% of that number
train_hours = int(df.index.nunique() * 0.7)

#Split train and test sets using index values for slicing
train = df[df.index <= df.index[train_hours]].copy()
test = df[df.index > df.index[train_hours]].copy()
train


# %% [markdown]
# VISUALIZATION

# %%
#Plotting train and test sets visualization 
fig, ax = plt.subplots(figsize = (15,10))
train.plot(ax=ax, label='Training Set', title='Train/Test Split of Ontario MW Demand')
test.plot(ax=ax, label='Test Set')
ax.axvline(df.index[train_hours], label = df.index[train_hours],color='red', ls='--')
ax.legend(['Training Set', 'Test Set', df.index[train_hours]])
plt.show()

# %% [markdown]
# FEATURE CREATION - HOLIDAYS

# %%
#Import Canadian holidays dataset (pulled from https://github.com/uWaterloo/Datasets/blob/master/Holidays/holidays.csv)
holidays = pd.read_csv("Canadian_Holidays_Data/holidays.csv")
holidays['date'] = pd.to_datetime(holidays["date"], format="%Y-%m-%d")
holidays = holidays.set_index('date')
holidays

# %% [markdown]
# FEATURE CREATION - TEMPERATURE

# %%


# %%
#Train feature creation by breaking down hourly MW datetime index into time components
train['Year'] = train.index.year
train['Month'] = train.index.month
train['DayOfMonth'] = train.index.day
train['DayOfYear'] = train.index.dayofyear
train['Hour'] = train.index.hour
train['DayOfWeek'] = train.index.dayofweek
train['WeekOfYear'] = train.index.isocalendar().week
train['Quarter'] = train.index.quarter

#Create holiday feature by setting holiday dates to true and non holidays to false 
train['Holiday'] = train.index.date
train['Holiday'] = train['Holiday'].isin(holidays.index.date).astype(bool)

#Test feature creation by breaking down hourly MW datetime index into time components
test['Year'] = test.index.year
test['Month'] = test.index.month
test['DayOfMonth'] = test.index.day
test['DayOfYear'] = test.index.dayofyear
test['Hour'] = test.index.hour
test['DayOfWeek'] = test.index.dayofweek
test['WeekOfYear'] = test.index.isocalendar().week
test['Quarter'] = test.index.quarter

#Create holiday feature by setting holiday dates to true and non holidays to false 
test['Holiday'] = test.index.date
test['Holiday'] = test['Holiday'].isin(holidays.index.date).astype(bool)

test.head(5000)

# %% [markdown]
# TRAINING

# %%
#Training XGBoost model

#Assigning independent and dependent variables to dataframes
train_features = train[['Year', 'Month', 'DayOfMonth', 'DayOfYear', 'Hour', 'DayOfWeek', 'WeekOfYear', 'Quarter', 'Holiday']]
train_target = train['Ontario Demand']

test_features = test[['Year', 'Month', 'DayOfMonth', 'DayOfYear', 'Hour', 'DayOfWeek', 'WeekOfYear', 'Quarter', 'Holiday']]
test_target = test['Ontario Demand']

# %%
#establishing model parameters and training model
model = xgb.XGBRegressor(n_estimators=5000, early_stopping_rounds=50, learning_rate=0.01)
model.fit(train_features, train_target, eval_set=[(train_features, train_target), (test_features, test_target)], verbose=100)

# %%
#Checking baseline RMSE
prediction_mean = np.mean(train_target)
baseline_rmse = root_mean_squared_error(train_target, np.full_like(train_target, prediction_mean))
print("Baseline RMSE (mean prediction): " + str(baseline_rmse))

# %% [markdown]
# TESTING MODEL

# %%
#predicting MW demand for test set
test['Predicted Demand'] = model.predict(test_features)
#Calculating RMSE for test set predictions
test_RMSE = root_mean_squared_error(test_target, test['Predicted Demand'])
print(test_RMSE)
test

# %% [markdown]
# FEATURE IMPORTANCE

# %%
#Examining feature importance
plot_importance(model, importance_type='gain', max_num_features=10, height=0.5)
plt.title("Most impactful features")
plt.tight_layout()
plt.show()


