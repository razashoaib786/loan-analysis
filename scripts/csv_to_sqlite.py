# scripts/csv_to_sqlite.py
import pandas as pd
import sqlite3

csv_path = "data/loan_data.csv"
db_path = "data/loan_data.db"
table_name = "loans"

df = pd.read_csv(csv_path)
# optional: basic cleaning
df['Loan_Status'] = df['Loan_Status'].map({'Y':'Y','N':'N'})  # keep as text
# write to sqlite
conn = sqlite3.connect(db_path)
df.to_sql(table_name, conn, if_exists="replace", index=False)
conn.close()
print("Saved to", db_path)
