import pandas as pd
import warnings

warnings.filterwarnings("ignore")

loan_status_data = pd.read_csv("loan_status.csv")

print("Statistics:")
print(loan_status_data.describe())

print("\nBlank Values:")
print(loan_status_data.isnull().sum())
