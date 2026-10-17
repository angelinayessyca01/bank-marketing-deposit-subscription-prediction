import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():
    with st.form('Prediksi Berlangganan Deposito'):
        
        # Load dan Baca Dataset
        df = pd.read_csv('bank-additional.csv',sep = ";")
        
        # Chart 1
        # Bar Plot
        st.write('Distribution of Deposit Status')
        fig = plt.figure(figsize = (10, 5))
        sns.countplot(x = 'y', data = df)
        st.pyplot(fig)
        
        # Chart 2
        # Histogram
        st.write('Plot Histogram for Numerical Features')
        fig = plt.figure(figsize = (10, 5))
        options = st.selectbox("Select Column for Histogram", ('age', 'duration', 'campaign'))
        sns.histplot(df[options], bins = 20, kde = True)
        st.pyplot(fig)
        
        # Chart 3, plotly express
        st.write('Scatterplot for Age & Contact Duration')
        fig = px.scatter(df, x = 'age', y = 'duration', hover_data = (['job', 'marital']))
        st.plotly_chart(fig)

if __name__ == "__main__":
    run()