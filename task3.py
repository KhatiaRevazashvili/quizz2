import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

loan_status_data = pd.read_csv("loan_status.csv")


plt.figure(figsize=(8, 6))
sns.distplot(loan_status_data['LoanAmount'], bins=20, kde=False, color='blue')
plt.title('Distribution of Loan Amount')
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.show()


plt.figure(figsize=(8, 6))
plt.hist(loan_status_data['ApplicantIncome'], bins=10, color='green')
plt.title('Histogram of Applicant Income')
plt.xlabel('Applicant Income')
plt.ylabel('Frequency')
plt.show()
