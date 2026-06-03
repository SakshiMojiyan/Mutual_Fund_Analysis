import pandas as pd
import os

folder_path = r"C:\Users\91783\Desktop\Mutual_Fund_Analysis\data\raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder_path, file))
        print(file, df.shape)
        print("\nData Types:",df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        # Missing Values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Duplicate Rows
        print("\nDuplicate Rows:",df.duplicated().sum())
        print("="*80)

