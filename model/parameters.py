import numpy as np
import random

TARGET_COL = 'Loan_Status'



# Define ordinal features and their category orders
ORDINAL_CAT_FEATURES = ['Dependents']
ORDINAL_CAT_ORDER = ['0', '1', '2', '3+']

# # Define the order for each ordinal feature
# ORDINAL_CAT_ORDER = {
#     'Dependents': ['0', '1', '2', '3+'],
#     'Loan_Amount_Term': ['short_term', 'medium_term', 'long_term'],
#     'Property_Area': ['0', '1', '2']
# }

# # Function to convert loan term values to categories
# def categorize_loan_term(term):
#     if term <= 100:
#         return 'short_term'
#     elif 100 < term <= 200:
#         return 'medium_term'
#     else:
#         return 'long_term'

# Example usage in preprocessing:
#df['Loan_Amount_Term'] = df['Loan_Amount_Term'].apply(categorize_loan_term)

CATEGORICAL_FEATURES = ['Property_Area']

BINARY_FEATURES = ['Gender', 'Credit_History', 'Self_Employed', 'Education', 'Married']

CONTINUOUS_FEATURES = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Property_Area']

COMBINED_FEATURES = ORDINAL_CAT_FEATURES + CATEGORICAL_FEATURES + CONTINUOUS_FEATURES
