# Projects
Collection of projects and files

* Ontario_MW_Project: Created as a learning experience using various resources and trial and error. 
  - Imported yearly .csv MW Demand data from IESO website
  - Concatenated these files into df
  - Set hourly datetime as index
  - Divided hourly demand into 70/30 test/train split
  - Graphed this split
  - imported historical Canadian holiday .csv
  - Set boolean holiday Y/N feature and divided datetime into various features to use for training model
  - Trained XGBoost model using 5000 estimators and 50 early stopping rounds, with a 0.01 learning rate
  - Output RMSE score of 1208 (Unsure but assuming strong considering MW hourly demand >15,000 MW?)
  - Compared training results to baseline RMSE of 2338
  - Tested model with RMSE of 1189
  - examined feature importance using xgb plot_importance

* Option Pricing Senior Project:
  - Created .pdf of group senior project
  - Examined the mathematics of popular option pricing models including Black-Scholes, Heston, Rough Heston, and Heston with Jumps.
  - Investigated strengths and weaknesses of each model
  - Investigated these models through various .py and MATLAB scripts
  - Received very positive feedback on the submission from evaluating mathematics professors
