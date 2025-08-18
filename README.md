# Projects
Collection of projects and files

* Crypto_Forecast: Created as a learning experience using online resources, tutorial, and trial and error.
  - Imported Yahoo Finance Bitcoin pricing data for last 10 years (2015-2025)
  - Kept daily close price, corresponding date, assigned past 3 days closing price as features
  - Scaled current and lag closing prices
  - Separated train/validation/test data into 70/20/10 split
  - Trained tensorflow NN model using Adam optimizer, mean squared error loss and mean average error loss metric
  - Trained model with 100 epochs, analyzed training vs validation loss, error minimized at epoch 94 (graphed)
  - Plotted train, validation, and test data
  - Predicted next day BTC price using trained NN model.
  - Prediction very innacurate ($103k USD prediction, current BTC value at $116k USD)

* Ontario_MW_Project: Created as a learning experience using various resources and trial and error. 
  - Imported historical hourly Ontario MW (electricity) demand data from IESO database (.csv)
  - Imported historical Canadian holiday dates (.csv)
  - Imported historical daily average temperatures from weather stations dispersed across Ontario (.csv)
  - Divided hourly demand into 70/30 test/train split (with visualization)
  - Created test/ train features (date and time, is holiday (Y/N), daily avg temperature) for each hour of MW demand
  - Trained XGBoost model using 5000 estimators and 50 early stopping rounds, with a 0.01 learning rate
  - Initial output RMSE score of 1208, with improvement to 1034 with avg temp feature added
  - Compared training results to baseline RMSE of 2338
  - Tested model with RMSE of 1032
  - ranked feature importance using xgb plot_importance

* Option Pricing Senior Project:
  - Submitted as senior year group research project
  - Examined the mathematics of popular option pricing models including Black-Scholes, Heston, Rough Heston, and Heston with Jumps.
  - Investigated strengths and weaknesses of each model
  - Investigated these models through various .py and MATLAB scripts
  - Received overwhelmingly positive feedback on the submission from evaluating mathematics professors
