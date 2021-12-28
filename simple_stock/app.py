import yfinance as yf
import streamlit as st
import pandas as pd
import datetime as dt


st.title("Simple Stock App")



ticker_symbol = st.sidebar.selectbox("Which stoock would you like to keep track of?", ('AAPL','MSFT','GOOG','FB','AMZN','TSLA','OTHER'))
if ticker_symbol=='OTHER':
    ticker_symbol=st.sidebar.text_input("Enter the stock symbol","For example: AAPL")
st.sidebar.write("You selected: ", ticker_symbol)
ticker_data = yf.Ticker(ticker_symbol)


today = dt.date.today()
year_ago = today - dt.timedelta(days=365)

start_date = st.sidebar.date_input("Start Date", value=year_ago)
end_date = st.sidebar.date_input("End Date", value=today)
ticker_dataframe = ticker_data.history(period="1d", start=start_date, end=end_date)

if end_date > start_date:
    st.sidebar.success('Start date: %s\n\nEnd date: %s' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')


caption = 'Stock prices for %s from %s to %s' % (ticker_symbol, start_date, end_date)
st.write(caption)

st.line_chart(ticker_dataframe.Close)
st.line_chart(ticker_dataframe.Open)
st.line_chart(ticker_dataframe.High)
st.line_chart(ticker_dataframe.Low)
st.line_chart(ticker_dataframe.Volume)
