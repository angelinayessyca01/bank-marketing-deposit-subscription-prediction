import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load all files
with open('model.pkl', 'rb') as file_1:
  model_rf = pickle.load(file_1)

with open('windsoriser.pkl', 'rb') as file_2:
  windsoriser = pickle.load(file_2)

with open('label_encoder.pkl','rb') as file_3:
  label_encoder = pickle.load(file_3)
  
def run():
    with st.form('Prediksi Berlangganan Deposito'):
        age = st.number_input('Age :', min_value = 18, max_value = 100)
        job = st.selectbox(
            'Job :', ('admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown')
        )
        marital = st.selectbox(
            'Marital Status :', ('divorced', 'married', 'single', 'unknown')
        )
        education = st.selectbox(
            'Education :', ('basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'professional.course', 'university.degree', 'unknown')
        )
        default = st.selectbox(
            'Credit Default :', ('no', 'unknown', 'yes')
        )
        housing = st.selectbox(
            'Housing Loan :', ('no', 'unknown', 'yes')
        )
        loan = st.selectbox(
            'Personal Loan :', ('no', 'unknown', 'yes')
        )
        contact = st.selectbox(
            'Contact Type :', ('cellular', 'telephone')
        )
        month = st.selectbox(
            'Last Contact Month :', ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
        )
        day_of_week = st.selectbox(
            'Last Contact Day :', ('mon', 'tue', 'wed', 'thu', 'fri')
        )
        duration = st.number_input(
            'Last Contact Duration :', min_value = 0, max_value = 3000
        )
        campaign = st.number_input(
            'Number of Contacts During This Campaign :', min_value = 1, max_value = 39
        )
        pdays = st.number_input(
            'Days Since Previous Contact :', min_value = 0, max_value = 999
        )
        previous = st.number_input(
            'Number of Previous Contacts :', min_value = 0, max_value = 15
        )
        poutcome = st.selectbox(
            'Previous Campaign Outcome :', ('failure', 'nonexistent', 'success')
        )
        emp_var_rate = st.number_input('Employment Variation Rate :')
        cons_price_idx = st.number_input('Consumer Price Index :')
        cons_conf_idx = st.number_input('Consumer Confidence Index :')
        euribor3m = st.number_input('Euribor 3 Month Rate :')
        nr_employed = st.number_input('Number of Employees :')
        
        submit = st.form_submit_button('Predict')
        
        data_inf = {
            'age' : age,
            'job' : job,
            'marital' : marital,
            'education' : education,
            'default' : default,
            'housing' : housing,
            'loan' : loan,
            'contact' : contact,
            'month' : month,
            'day_of_week' : day_of_week,
            'duration' : duration,
            'campaign' : campaign,
            'pdays' : pdays,
            'previous' : previous,
            'poutcome' : poutcome,
            'emp.var.rate' : emp_var_rate,
            'cons.price.idx' : cons_price_idx,
            'cons.conf.idx' : cons_conf_idx,
            'euribor3m' : euribor3m,
            'nr.employed' : nr_employed
        }
        
        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf)
        
        if submit:
            # Mengubah nilai 999 pada pdays menjadi missing value
            data_inf['pdays'] = data_inf['pdays'].replace(999, np.nan)

            # Menangani outlier menggunakan winsoriser yang sudah dilatih
            data_inf = windsoriser.transform(data_inf)

            # Menghapus fitur duration
            data_inf = data_inf.drop(['duration'], axis = 1)
            
            # Melakukan prediksi menggunakan Random Forest
            y_pred_inf = model_rf.predict(data_inf)
            
            # Mengembalikan hasil prediksi menjadi no atau yes
            y_pred_inf_label = label_encoder.inverse_transform(y_pred_inf)
            
            st.write('### Deposit Prediction :', y_pred_inf_label[0])
            
if __name__ == '__main__':
    run()