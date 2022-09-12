import streamlit as st
import json
import pandas as pd
import plotly.express as px
import requests

def get_data():
    url = "https://api.covid19api.com/country/singapore"
    res = requests.get(url)
    response_dict = json.loads(res.content)
    return pd.DataFrame(response_dict)

st.header("Covid 19 cases in SG")

with st.spinner('Getting data...'):
    df = get_data()
    st.success("Sucessfully retrieved data")

fig = px.line(df, x='Date', y="Confirmed")
st.plotly_chart(fig)