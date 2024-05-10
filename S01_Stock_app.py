import streamlit as st
import pandas as pd
import yfinance as yf
import datetime as dt

# from streamlit_jupyter import StreamlitPatcher, tqdm

# import os
# import sys
# os.path.dirname(sys.executable)
# print(os.getcwd())


st.write("""
# Simple Stock Price App

Shown are the stock **Close price** and **Volume of Apple!**

""")

symbol = 'AAPL'
start_date = '2010-01-01'
end_date = dt.date.today()

tickerDf = yf.download(symbol, start=start_date, end=end_date)

st.write("""
## Close Price
""")
st.line_chart(tickerDf['Close'])
st.write("""
## Volume Price
""")
st.line_chart(tickerDf['Volume'])