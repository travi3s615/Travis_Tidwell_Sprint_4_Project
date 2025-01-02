import streamlit as st
import pandas as pd
from plotly import express as px


df = pd.read_csv("vehicles_us.csv")

st.dataframe(df.head(10))

st.write("### Price Distribution")
fig = px.histogram(df, x='price', title='Distribution of Prices')
st.plotly_chart(fig)

st.write("### Price vs Year")
scatter = px.scatter(df, x='year', y='price', title='Price vs Year')
st.plotly_chart(scatter)

if st.checkbox("Show Raw Data"):
    st.write(df)
    
