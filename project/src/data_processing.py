
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # Example for data preprocessing
    df.fillna(0, inplace=True)
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
