import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

#Titles
st.title("Crypto Daily Prices")
st.header("Dashboard")

#Define Crypto Tickers
Bitcoin = 'BTC=USD'
Ethereum = 'ETH=USD'
Ripple = 'XRP=USD'

#Yfinance data
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)

#Retrieve the Yfinance Data for Crypto
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")

#dataframe for crypto data
BTC = yf.download(Bitcoin, start="2024-03-13", end="2024-03-14")
ETH = yf.download(Ethereum, start="2024-03-13", end="2024-03-14")
XRP = yf.download(Ripple, start="2024-03-13", end="2024-03-14")

#BTC
st.write("Bitcoin")
st.table(BTC)
st.bar_chart(BTCHis.Close)

#ETH
st.write("Ethereum")
st.table(ETH)
st.bar_chart(ETHHis.Close)

#XRP
st.write("Ripple")
st.table(XRP)
st.bar_chart(XRPHis.Close)

