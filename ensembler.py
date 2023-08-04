import pandas as pd

# List of dataframe filenames
dataframe_filenames = [
    "gb_latest.csv",
    "lg_latest.csv",
    "nn_new03.csv",

]

# List to store the dataframes
prediction_dfs = []

# Loop to read the dataframes
for filename in dataframe_filenames:
    pred_df = pd.read_csv(filename)
    prediction_dfs.append(pred_df)

# Combine the ID column from any of the DataFrames (assuming they are the same)
ensemble_df = prediction_dfs[0][['ID']].copy()

# Perform ensemble averaging
for i, pred_df in enumerate(prediction_dfs, start=1):
    ensemble_df[f'price_pred_{i}'] = pred_df['price']

# Calculate the average of predictions across all models
ensemble_df['ensemble_price'] = ensemble_df.iloc[:, 1:].mean(axis=1)

# Now, ensemble_df contains the ID column and predictions from all models, along with the ensemble prediction.
# You can save this DataFrame to a CSV file or use it for further analysis.
sub_df = ensemble_df[['ID']].copy()
sub_df['price'] = ensemble_df['ensemble_price']
sub_df.to_csv('ensemble_latest.csv',index =False)