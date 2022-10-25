import streamlit as st
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
import yfinance as yf
import datetime
import pandas as pd

st.set_page_config(page_title="Stock Price Analysis and Prediction", page_icon="chart_with_upwards_trend", 
                        layout="centered", initial_sidebar_state = "auto")

list_sectors = []
list_sectors.append('Basic Materials')
list_sectors.append('Communication Services')
list_sectors.append('Consumer Cyclical')
list_sectors.append('Consumer Defensive')
list_sectors.append('Energy')
list_sectors.append('Financial Services')
list_sectors.append('Healthcare')
list_sectors.append('Industrials')
list_sectors.append('Real Estate')
list_sectors.append('Technology')
list_sectors.append('Utilities')
#list_sectors

ticker_list = si.tickers_nasdaq()

df1 = pd.read_csv('data/basic_materials_ticker_list.csv')['Basic Materials']
list_bm = df1.values.tolist()
df2 = pd.read_csv('data/communication_services_ticker_list.csv')['Communication Services']
list_cs = df2.values.tolist()
df3 = pd.read_csv('data/consumer_cyclical_ticker_list.csv')['Consumer Cyclical']
list_cc = df3.values.tolist()
df4 = pd.read_csv('data/consumer_defensive_ticker_list.csv')['Consumer Defensive']
list_cd = df4.values.tolist()
df5 = pd.read_csv('data/energy_ticker_list.csv')['Energy']
list_en = df5.values.tolist()
df6 = pd.read_csv('data/financial_services_ticker_list.csv')['Financial Services']
list_fs = df6.values.tolist()
df7 = pd.read_csv('data/healthcare_ticker_list.csv')['Healthcare']
list_hc = df7.values.tolist()
df8 = pd.read_csv('data/industrials_ticker_list.csv')['Industrials']
list_id = df8.values.tolist()
df9 = pd.read_csv('data/real_estate_ticker_list.csv')['Real Estate']
list_re = df9.values.tolist()
df10 = pd.read_csv('data/technology_ticker_list.csv')['Technology']
list_tc = df10.values.tolist()
df11 = pd.read_csv('data/utilities_ticker_list.csv')['Utilities']
list_ut = df11.values.tolist()

st.markdown("""# *Finance Data Analysis*""")

currentDate = datetime.date.today()
firstDayOfMonth = datetime.date(currentDate.year, currentDate.month, 1)

title_col1,title_col2,title_col3 = st.columns([3,3,3])
with title_col1:
    sector_name = st.selectbox('Select Sector :',list_sectors,index = 0)
with title_col2:
    if sector_name == "Basic Materials":
        ticker_name = st.selectbox('Select Ticker :',list_bm,index = 0)
    if sector_name == "Communication Services":
        ticker_name = st.selectbox('Select Ticker :',list_cs,index = 0)
    if sector_name == "Consumer Cyclical":
        ticker_name = st.selectbox('Select Ticker :',list_cc,index = 0)
    if sector_name == "Consumer Defensive":
        ticker_name = st.selectbox('Select Ticker :',list_cd,index = 0)
    if sector_name == "Energy":
        ticker_name = st.selectbox('Select Ticker :',list_en,index = 0)
    if sector_name == "Financial Services":
        ticker_name = st.selectbox('Select Ticker :',list_fs,index = 0)
    if sector_name == "Healthcare":
        ticker_name = st.selectbox('Select Ticker :',list_hc,index = 0)
    if sector_name == "Industrials":
        ticker_name = st.selectbox('Select Ticker :',list_id,index = 0)
    if sector_name == "Real Estate":
        ticker_name = st.selectbox('Select Ticker :',list_re,index = 0)
    if sector_name == "Technology":
        ticker_name = st.selectbox('Select Ticker :',list_tc,index = 0)
    if sector_name == "Utilities":
        ticker_name = st.selectbox('Select Ticker :',list_ut,index = 0)
    
with title_col3:
    pass

title_col1,title_col2,title_col3 = st.columns([3,3,3])
with title_col1:
    st_date = st.date_input('Start Date :', firstDayOfMonth, datetime.date(1980, 1, 1), currentDate)
with title_col2:
    en_date = st.date_input('End Date :',currentDate)
with title_col3:
    interval_option = st.selectbox(
        'Time Interval',
        ('Day', 'Month'))

if interval_option == "Month":
    interval_option = "1mo"
else :
    interval_option = "1d"

ticker_details = get_data(ticker_name, start_date=st_date, end_date=en_date, index_as_date = True, interval=interval_option)
df = ticker_details
df['daily_pc_returns'] = (df['close']/df['close'].shift(1) - 1) * 100
df['daily_pc_returns'] = round(df['daily_pc_returns'], 2)
if (len(ticker_details) > 0):
    st.subheader(f'{ticker_name} Stock Data')
    st.dataframe(df.tail(), 1500, 210)
    st.line_chart(df.daily_pc_returns)
else:
    st.write("No Data Found!")

