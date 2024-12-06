# BlueChip_Project_Credit_worthiness_Classification_Analysis

# Credit Analysis Project

## Overview

This project involves building a machine learning model to predict loan approval status based on various applicant features. The dataset includes information about applicants' income, loan amount, credit history, and other demographic details. The goal is to create a robust model that can accurately predict whether a loan will be approved or not.

## Dataset

The dataset consists of two files: `Train.csv` and `Test.csv`. The training dataset is used to train the model, while the test dataset is used to evaluate its performance.

### Features

- **Numeric Features**:
  - `Total_Income`
  - `Loan_Amount_Term`
  - `LoanAmount`
  - `CoapplicantIncome`
  - `ApplicantIncome`
  - `ID`

- **Categorical Features**:
  - `Loan_Status` (Target)
  - `Property_Area`
  - `Credit_History`
  - `Self_Employed`
  - `Education`
  - `Dependents`
  - `Married`
  - `Gender`

## Data Preprocessing

### Handling Missing Values

Missing values in the dataset are handled by imputing or removing them as necessary.

### Feature Engineering

Several new features are created to enhance the model's predictive power:

- `Income_Per_Dependent`: Applicant's income divided by the number of dependents.
- `Income_Stability`: Adjusted applicant income based on employment status and credit history.
- `Income_Loan_Ratio`: Ratio of total income to loan amount.
- `Loan_Term_Category`: Binned loan term into short-term, mid-term, and long-term.
- `Income_Category`: Binned applicant income into low, mid, and high.
- `Zero_Coincome_Low_Appincome`: Indicator for applicants with zero co-applicant income and low applicant income.
- `Loan_Size_Category`: Binned loan amount into small, mid, and large.

### Scaling

Numeric features are scaled using MinMaxScaler to normalize the data.

### Encoding Categorical Features

Categorical features are encoded using one-hot encoding to convert them into a format suitable for machine learning algorithms.

## Exploratory Data Analysis (EDA)

EDA is performed to understand the distribution of features and their relationship with the target variable. Various plots are generated to visualize the data:

- Distribution of categorical features using bar charts and pie charts.
- Loan approval rates based on different features and credit history.

### Insights

1. Women with credit history of 1 have an 83.65% positive approval rate.
2. Women with 0 credit history score have an 85.71% approval rate, which is higher than that of men.
3. Educated applicants with a credit history score of 1 have an 82.29% approval rate compared to 83.45% for uneducated applicants. Uneducated businessmen in Nigeria tend to be more trusted.
4. Uneducated applicants with 0 credit history have an 83.37% approval rate compared to 81.48% for educated applicants.
5. Married applicants with credit history of 1 have an 83.22% approval rate, while unmarried applicants have a higher approval rate of 83.86%.
6. Married applicants with 0 credit history have an 82.66% approval rate compared to 85.92% for unmarried applicants.
7. Applicants with property in urban areas and credit history of 1 have an 84.68% approval rate compared to 82.77% for suburban and 81.86% for rural areas.
8. Applicants with credit history of 0 and property in suburban areas have an 85% approval rate compared to 82.22% for urban and 80.90% for rural areas.
9. Applicants with credit history of 1 and 0 dependents have an 84.05% approval rate compared to 82.40%, 82.71%, and 80.84% for 1, 2, and 3+ dependents, respectively.
10. People with 3+ dependents and credit history of 0 have a 91.11% approval rate, followed by 1 dependent at 83.13%, 0 dependents at 82.81%, and 2 dependents at 78.57%.
11. Applicants with credit history of 1 who are self-employed have an 84.16% approval rate compared to 83.21% for those who are not self-employed.
12. Applicants with credit history of 0 who are self-employed have an 81.25% approval rate compared to 83.37% for those who are not self-employed.
13. Applicants with credit history of 1 asking for short-term loans have an 83.87% approval rate compared to 80.56% for mid-term and 83.32% for long-term loans.
14. Applicants with 0 credit history asking for mid-term loans had a 100% loan approval rate, while those asking for mid-term loans had a rejection rate of 66.67%, and those asking for long-term loans had an 83.62% approval rate.
15. 16.31% of 4789 is 781 loan declines, 80% of the total loan decline of 985. This category holds 80% of loan declines for applicants with 0 co-applicant income and low applicant income.

## Model Building

### Resampling

To address class imbalance, the following resampling techniques are used:

- **SMOTE (Synthetic Minority Over-sampling Technique)**: To oversample the minority class.
- **Random Under-sampling**: To undersample the majority class.

### Model Training

Three different models are trained and evaluated:

1. **XGBoost Classifier**
2. **Random Forest Classifier**
3. **CatBoost Classifier**

### Hyperparameter Tuning

Grid search is used to find the best hyperparameters for each model.

### Model Evaluation

The models are evaluated using the following metrics:

- F1 Score
- ROC AUC Score
- Precision
- Recall
- Confusion Matrix

### Voting Classifier

A voting classifier is created using the three models to improve overall performance. The voting classifier uses soft voting to combine the predictions of the individual models.

## Results

The performance of the models is evaluated on the test set, and the results are presented using confusion matrices and evaluation metrics.

## Conclusion

The project demonstrates the application of various machine learning techniques to build a robust model for credit analysis. The use of feature engineering, resampling techniques, and ensemble methods helps in improving the model's accuracy and reliability.

## Future Work

- Further tuning of hyperparameters to improve model performance.
- Exploration of additional features and data sources.
- Deployment of the model as a web service for real-time predictions.
