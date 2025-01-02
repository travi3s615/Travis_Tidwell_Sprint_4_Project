import streamlit as st
import pandas as pd
from plotly import express as px

st.write("Hello, world!")

df = pd.read_csv("vehicles_us.csv")

st.table(df)