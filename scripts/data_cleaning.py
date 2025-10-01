# data_cleaning.py
import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Example: fill missing LoanAmount with median
    df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
    # Encode Loan_Status: Y=1, N=0
    df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})
    return df

if __name__ == "__main__":
    df = load_data("data/loan_data.csv")
    df = clean_data(df)
    df.to_csv("data/loan_data_cleaned.csv", index=False)
    print("✅ Cleaned data saved to data/loan_data_cleaned.csv")
