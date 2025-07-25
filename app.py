
import streamlit as st
from client import STOCKAPI
 
# Create page
st.set_page_config("STOCK MARKET DATA PLOTING" ,  layout="wide")
 
# add title
 
st.title("Stock Market app for Candelstick chart")
st.subheader("By Aishwarya Khune ")
 
 
# create function to fetch data
@st.cache_resource(ttl = 3600)
def fetch_data():
    return  STOCKAPI(api_key= st.secrets["API_KEY"])
 
stock_api  =  fetch_data()
 
# take company  name  from user
 
company  =  st.text_input("Enter Company Name here")
 
# create function to get symbol
@st.cache_data(ttl =  3600)
def get_symbol(company_name):
    return  stock_api.symbol_search(company_name)
 
 
# create method to plot the chart
@st.cache_data(ttl  =  3600)
def get_plot(symbol):
    df =  stock_api.Time_Series_Daily(symbol)
    fig =  stock_api.candelstick_chart(df)
    return  fig
 
 
# make it functional
 
if company :
 
    company_data  =  get_symbol(company)
 
    if company_data:
         symbols  =  list(company_data.keys())
         option  =  st.selectbox("Enter symbol here" ,  symbols)
 
         compnay_info  =  company_data[option]
 
         st.success(f"**Company Name**:  {compnay_info[0]}")
         st.success(f"**Company Region**:  {compnay_info[1]}")
         st.success(f"**Currency**:  {compnay_info[2]}")
 
         plot = st.button("Submit" ,  type  = "primary")
 
         if plot :
             fig = get_plot(option)
             st.plotly_chart(fig)
             
    else:
        st.subheader("Company Does Not Exists")
 
 
 