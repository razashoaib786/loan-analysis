# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_model(path):
    df = pd.read_csv(path)
    # Features: ApplicantIncome, CoapplicantIncome, LoanAmount
    X = df[['ApplicantIncome','CoapplicantIncome','LoanAmount']].fillna(0)
    y = df['Loan_Status']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("✅ Model Accuracy:", accuracy_score(y_test, preds))
    return model

if __name__ == "__main__":
    train_model("data/loan_data_cleaned.csv")
