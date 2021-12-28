import yfinance as yf
import streamlit as st
import pandas as pd


st.title("Stock Price App")
st.write("""
         Shown are the stock prices of the selected stock.
         """)


ticker_symbol = st.selectbox("Which stoock would you like to keep track of?", ('AAPL','MSFT','GOOG','FB','AMZN','TSLA','OTHER'))
if ticker_symbol=='OTHER':
    ticker_symbol=st.text_input("Enter the stock symbol","For example: AAPL")
st.write("You selected: ", ticker_symbol)
ticker_data = yf.Ticker(ticker_symbol)
ticker_dataframe = ticker_data.history(period="1d", start="2020-01-01", end="2020-04-01")
st.line_chart(ticker_dataframe.Close)
st.line_chart(ticker_dataframe.Open)
st.line_chart(ticker_dataframe.High)
st.line_chart(ticker_dataframe.Low)
st.line_chart(ticker_dataframe.Volume)