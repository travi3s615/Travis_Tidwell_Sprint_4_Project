import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.dataframe(df.head(51))

st.write("### Price Distribution")
fig = px.histogram(df, x='price', title='Distribution of Prices')
st.plotly_chart(fig)

st.write("### Price vs Model Year")
scatter = px.scatter(df, x='model_year', y='price', title='Price vs Model Year')
st.plotly_chart(scatter)

if st.checkbox('Show Raw Data'):
    st.write(df)
