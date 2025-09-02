# Projects
*Collection of projects and files*

* Ontario_MW_Project: Created as a learning experience using various resources and trial and error 
  - Imported historical hourly Ontario MW (electricity) demand data from IESO database (.csv)
  - Imported historical Canadian holiday dates (.csv)
  - Imported Govt of Canada historical daily average temperatures from weather stations dispersed across Ontario (.csv)
  - Divided hourly demand into 70/30 test/train split (with visualization)
  - Created test/ train features (date and time, is holiday (Y/N), daily avg temperature) for each hour of MW demand
  - Trained XGBoost model using 5000 estimators and 50 early stopping rounds, with a 0.01 learning rate
  - Initial output RMSE score of 1208, with improvement to 1034 with avg temp feature added
  - Compared training results to baseline RMSE of 2338
  - Tested model with RMSE of 1032
  - ranked feature importance using xgb plot_importance
  - *Learning Summary*:
    - Hourly average temperature data preferred to daily average temperature but was impossible to find. Considering hour of day was most impactful feature, I believe associated hourly temperature would greatly increase   model accuracy
    - Many weather stations lacked recent data, uniform temperature coverage of Ontario was difficult to find. Attempted to provide adequate coverage of the province while pulling data primarily from weather stations centered in locations with elevated population
    - Trial and error with many combinations of XGB parameters proved more trees (n_estimators = 5000 vs. 1000, 2000 etc.) coupled with lower learning rate (learning_rate = 0.01 vs. 0.1, 0.05 etc.) decreased training and test RMSE while early stopping rounds prevented overfitting
    - *Feature importance*:
      - Hour of Day: As most impactful feature, proves morning and evening residential/ commercial demand overlap (and decrease in demand overnight) greatly impacts forecasted demand
      - Temperature: As 2nd most impactful feature, even daily avg temp (lacking hourly fluctuations) proves that temperature (and associated climate control appliance use) greatly influences electricity demand
      - Holiday: As 3rd most impactful feature, proves increased/ sustained residential demand and holiday-specific demand (sporting events, christmas lights, etc.) over holidays have an impact on electricitry demand
      - Month/Day of Month: As least impactful features, intuitively fluctuations in temp for a specific month year to year leads to little impact on electricity demand forecasting. Day of month does not give info on  
         
* Crypto_Forecast: Created as a learning experience using online resources, tutorial, and trial and error.
  - Imported Yahoo Finance Bitcoin pricing data for last 10 years (2015-2025)
  - Kept daily close price, corresponding date, assigned past 3 days closing price as features
  - Scaled current and lag closing prices
  - Separated train/validation/test data into 70/20/10 split
  - Trained tensorflow NN model using Adam optimizer, mean squared error loss and mean average error loss metric
  - ^ with past 2 years vs. 10 years training optimal epoch now 65, should cut down training epochs
  - Plotted train, validation, and test data
  - Predicted next day BTC price using trained NN model
  - Prediction very innacurate ($103k USD prediction, current BTC value at $116k USD - more accurate predictions with 2 years training data)
  - *Learning Summary*:
    - Changing historical BTC pricing training set from last 10 years (2015-2025) to last 2 years (2023-2025) resulted in more accurate forecasting, most likely due to low pricing in early years which skews forecasts.
    - With 2 year vs. 10 year dataset, error minimized at epoch 65 vs. epoch 94. Should cut down number of training epochs to reduce computation time.
    - Considering long training times, plotting training/ validation loss seems worth the effort as allows for optimization with respect to number of epochs.
    - Potential overfitting of training data as reflected on training prediction vs. actual chart, however validation error does not increase. Will implement RMSE metric to examine.

* Option Pricing Senior Project:
  - Submitted as senior year group research project
  - Examined the mathematics of popular option pricing models including Black-Scholes, Heston, Rough Heston, and Heston with Jumps.
  - Investigated strengths and weaknesses of each model
  - Investigated these models through various .py and MATLAB scripts
  - Received overwhelmingly positive feedback on the submission from evaluating mathematics professors
