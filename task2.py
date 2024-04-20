import pandas as pd
import warnings

warnings.filterwarnings("ignore")

loan_status_data = pd.read_csv("loan_status.csv")

total_loans = len(loan_status_data)
approved_loans = len(loan_status_data[loan_status_data['Loan_Status'] == 'Y'])
probability_loan_approval = approved_loans / total_loans
print("sesxis aghebis albatoba:", probability_loan_approval)

good_credit_loans = len(loan_status_data[(loan_status_data['Loan_Status'] == 'Y') & (loan_status_data['Credit_History'] == 1)])
total_good_credit = len(loan_status_data[loan_status_data['Credit_History'] == 1])
probability_good_credit_loan = good_credit_loans / total_good_credit
print("sesxis aghebiss albatoba(kargi istoria):", probability_good_credit_loan)
