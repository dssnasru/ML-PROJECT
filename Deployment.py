# -*- coding: utf-8 -*-
"""
Created on 

@author:
"""

import pandas as pd
import streamlit as st
from datetime import date
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from pickle import dump
from pickle import load
from statsmodels.tsa.holtwinters import Holt

st.title('Gold Price Forecasting')

n_days = st.number_input("Enter number of days",0,150)
period = n_days

data = pd.read_csv(r"C:\Users\ELCOT\Gold Price\Gold_data.csv",date_parser=['date'])
st.subheader('Raw data')
st.write(data.tail())

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['date'], y=data['price'],name="data"))
	fig.layout.update(title_text='Time Series data', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
    
plot_raw_data()

## Load the model
loaded_model = load(open(r'C:\Users\ELCOT\Gold Price\hw_model.sav', 'rb'))
X=period
column_names = ['Price']
pred=pd.DataFrame(loaded_model.forecast(X),columns=column_names)
st.subheader('Forecasted data')
data1=pred
data1.reset_index(level=0, inplace=True)
data1.rename(columns = {'index':'date'}, inplace = True)
data1['date'] = pd.to_datetime(data1['date']).dt.date
data1
st.line_chart(data1['Price'])
