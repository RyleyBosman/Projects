# Projects
Collection of projects and files

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
