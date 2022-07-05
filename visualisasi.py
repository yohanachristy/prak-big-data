import yfinance as yf
import pandas as pd
import streamlit as st 
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


st.write("""
# Aplikasi Yahoo Finance
## Data Saham Google

Berikut ini adalah data closing price dan volume dari Google. 
""")

ticker = st.selectbox(
    "Ticker Perusahaan",
    options = [ "ANTM", "AAPL", "MSFT", "GOOG", "AMZN"]
) 
tickerData = yf.Ticker(ticker)

jumlah_hari = timedelta(days=-30)


tgl_mulai = st.date_input(
    "Mulai dari tanggal"
    value=date.today()+jumlah_hari
)

tgl_akhir = st.date_input(
    "Hingga"
    value=date.today()
)


# hard coded
tickerDF = tickerData.history(
    period='1d',
    start='2022-01-01',
    end=srt(tgl_akhir)
)


st.write(type(tickerDF))

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume) 

