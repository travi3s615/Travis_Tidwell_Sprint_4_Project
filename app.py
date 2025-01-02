import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

df['price'] = pd.to_numeric(df['price'], errors='coerce')

df = df.dropna(subset=['price'])

df['price'] = df['price'].astype(int)

df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')

df = df.dropna(subset=['model_year'])

df['model_year'] = df['model_year'].astype(int)

st.title("Vehicle Listings Analysis")

if st.checkbox("Show Raw Data"):
    st.write("### Raw Data")
    st.dataframe(df.head(51))

st.sidebar.header("Filter Options")

fuel_type = st.sidebar.selectbox("Select Fuel Type", options=df['fuel'].unique())

min_price, max_price = st.sidebar.slider(
    "Select Price Range", int(df['price'].min()), int(df['price'].max()), (5000, 20000)
)

filtered_data = df[(df['fuel'] == fuel_type) & (df['price'] >= min_price) & (df['price'] <= max_price)]

if filtered_data.empty:
    st.warning("No data matches the selected filters. Please adjust the filter criteria.")
else:
    
    st.write("### Price vs Model Year")
    scatter = px.scatter(
        filtered_data,
        x='model_year',
        y='price',
        title='Price vs Model Year',
        labels={'model_year': 'Model Year', 'price': 'Price ($)'}
    )
    st.plotly_chart(scatter)

    st.write("### Count of Cars by Fuel Type")
    bar_chart = px.bar(
        filtered_data,
        x='fuel',
        title='Count of Cars by Fuel Type',
        labels={'fuel': 'Fuel Type'},
        color='fuel'
    )
    st.plotly_chart(bar_chart)

    st.write("### Price Distribution by Condition")
    box_plot = px.box(
        filtered_data,
        x='condition',
        y='price',
        title='Price Distribution by Condition',
        labels={'condition': 'Condition', 'price': 'Price ($)'},
        color='condition'
    )
    st.plotly_chart(box_plot)

st.write("### Download Filtered Data")
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_data.to_csv(index=False),
    file_name='filtered_vehicles_data.csv',
    mime='text/csv'
)

st.write("### Insights")
st.markdown("""
- The **Price vs Model Year** scatter plot shows that newer vehicles generally have higher prices.
- The **Count of Cars by Fuel Type** bar chart highlights the distribution of vehicles by fuel type.
- The **Price Distribution by Condition** box plot indicates that vehicles in better condition tend to be priced higher.
""")
