import pandas as pd
import numpy as np
from src.exception import CustomExceptions
from src.logger import logging
import pickle
import streamlit as st
import os
import sys

model_path = r"C:\Users\ADMIN\OneDrive\Documents\adabost_model_path"

try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    if hasattr(model, 'predict'):
        st.success("Model loaded successfully.")
    else:
        st.error("The loaded object is not a valid machine learning model.")

except Exception as e:
    st.error(f"Failed to load the model from {model_path}")
    raise CustomExceptions(e, sys)
# Define the feature names
feature_names = ['member_id', 'loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'int_rate',
        'installment', 'grade', 'sub_grade', 'emp_title', 'emp_length',
        'home_ownership', 'annual_inc', 'verification_status', 'pymnt_plan',
        'purpose', 'title', 'zip_code', 'addr_state', 'dti', 'inq_last_6mths',
        'mths_since_last_delinq', 'open_acc', 'revol_bal', 'revol_util',
        'total_acc', 'initial_list_status', 'out_prncp', 'out_prncp_inv',
        'total_pymnt', 'total_pymnt_inv', 'total_rec_prncp', 'total_rec_int',
        'last_pymnt_amnt', 'policy_code', 'application_type', 'tot_cur_bal',
        'total_rev_hi_lim', 'issue_date_day', 'issue_date_month',
        'issue_date_year', 'last_pymnt_diff_next_pymnt_days',
        'last_pymnt_diff_next_pymnt_year']

# Streamlit UI
st.title("Credit Loan Risk Analysis.")
st.sidebar.header('Customer Data')
try:
# Input fields
    def member_info():
        member_id =st.sidebar.slider('member_id',80353,73518392,1)
        loan_amnt=st.sidebar.slider('loan_amnt',500,35000,1)
        funded_amnt=st.sidebar.slider('funded_amnt',500,35000,1)
        funded_amnt_inv=st.sidebar.slider('funded_amnt_inv',12,35000,1)
        int_rate=st.sidebar.slider('int_rate',5,28,1)
        installment=st.sidebar.slider('installment',15,1424,1)
        grade=st.sidebar.slider('grade',1,7,1)
        sub_grade=st.sidebar.slider('sub_grade',0,1,1)
        emp_title=st.sidebar.slider('emp_title',0,1,1)
        emp_length=st.sidebar.slider('emp_length',11,17,1)
        home_ownership=st.sidebar.slider('home_ownership',1,7,1)
        annual_inc=st.sidebar.slider('annual_inc',1200,8706582,1)
        verification_status=st.sidebar.slider('verification_status',0,2,1)
        pymnt_plan=st.sidebar.slider('pymnt_plan',0,0,1)
        purpose=st.sidebar.slider('purpose',1,14,1)
        title=st.sidebar.slider('title',0,1,1)
        zip_code=st.sidebar.slider('zip_code',7,999,1)
        addr_state=st.sidebar.slider('addr_state',0,50,1)
        dti=st.sidebar.slider('dti',0,9999,1)
        inq_last_6mths=st.sidebar.slider('inq_last_6mths',0,8,1)
        mths_since_last_delinq=st.sidebar.slider('mths_since_last_delinq',31,31,1)
        open_acc=st.sidebar.slider('open_acc',0,90,1)
        revol_bal=st.sidebar.slider('revol_bal',0,1746716,1)
        revol_util=st.sidebar.slider('revol_util',55,55,1)
        total_acc=st.sidebar.slider('total_acc',2,146,1)
        initial_list_status=st.sidebar.slider('initial_list_status',0,1,1)
        out_prncp=st.sidebar.slider('out_prncp',0,35000,1)
        out_prncp_inv=st.sidebar.slider('out_prncp_inv',0,35000,1)
        total_pymnt=st.sidebar.slider('total_pymnt',0,57777,1)
        total_pymnt_inv=st.sidebar.slider('total_pymnt_inv',0,57777,1)
        total_rec_prncp=st.sidebar.slider('total_rec_prncp',0,35000,1)
        total_rec_int=st.sidebar.slider('total_rec_int',0,23172,1)
        last_pymnt_amnt=st.sidebar.slider('last_pymnt_amnt',0,36257,1)
        policy_code=st.sidebar.slider('policy_code',0,1,1)
        application_type=st.sidebar.slider('application_type',0,0,1)
        tot_cur_bal=st.sidebar.slider('tot_cur_bal',81008,81008,1)
        total_rev_hi_lim=st.sidebar.slider('total_rev_hi_lim',23800,23800,1)
       # default_ind=st.sidebar.slider('default_ind',0,1,1)
        issue_date_day=st.sidebar.slider('issue_date_day',1,12,1)
        issue_date_month=st.sidebar.slider('issue_date_month',0,1,1)
        issue_date_year=st.sidebar.slider('issue_date_year',2007,2015,1)
        last_pymnt_diff_next_pymnt_days=st.sidebar.slider('last_pymnt_diff_next_pymnt_days',0,1,1)
        last_pymnt_diff_next_pymnt_year=st.sidebar.slider('last_pymnt_diff_next_pymnt_year',2015,2016,1)
        
        customer_report_data = {column: column for column in feature_names}
        report_data = pd.DataFrame.from_dict(customer_report_data, orient='index')
        return report_data
    user_data=member_info()
    st.header('Credit Loan Data')
    st.write(user_data)
except Exception as e:
    logging.info('Check data in progress')
    raise CustomExceptions(e,sys)
try:
    # Make a prediction
    if st.button("Predict"):
        prediction = model.predict(user_data)[0]
        if prediction == 0:
            st.write("Prediction: Not At Risk")
        else:
            st.write("Prediction: Defaulter is in Risk")
except Exception as e:
    logging.info('Complete Credit Loan Risk Analysis.')
    raise CustomExceptions(e,sys)
