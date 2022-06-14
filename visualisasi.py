import yfinance as yf
import pandas as pd
import streamlit as st 

st.write("""
# Aplikasi Yahoo Finance
## Data Saham Google

Berikut ini adalah data closing price dan volume dari Google. 
""")

ticker = 'GOOGL' 
tickerData = yf.Ticker(ticker)
tickerDF = tickerData.history(period='1d', start='2022-01-01', end='2022-05-30')

st.write(type(tickerDF))

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume) 

