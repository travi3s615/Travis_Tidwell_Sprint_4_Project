import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.dataframe(df.head(51))

st.sidebar.header("Filter Options")

fuel_type = st.sidebar.selectbox("Select Fuel Type", options=df['fuel'].unique())

min_price, max_price = st.sidebar.slider("Select Price Range", int(df['price'].min()), int(df['price'].max()), (5000, 20000))

filtered_data = df[(df['fuel'] == fuel_type) & (df['price'] >= min_price) & (df['price'] <= max_price)]

if filtered_data.empty:
    st.warning("No data matches the selected filters.")
else:
   
    st.write("### Price vs Model Year (Filtered)")
    scatter = px.scatter(filtered_data, x='model_year', y='price', title='Price vs Model Year (Filtered)')
    st.plotly_chart(scatter)

    st.write("### Count of Cars by Fuel Type")
    bar_chart = px.bar(df, x='fuel', title='Count of Cars by Fuel Type', color='fuel')
    st.plotly_chart(bar_chart)

    st.write("### Price Distribution by Condition")
    box_plot = px.box(df, x='condition', y='price', color='condition', title='Price Distribution by Condition')
    st.plotly_chart(box_plot)

if st.checkbox("Show Raw Data"):
    st.write(df)

st.write("### Download Filtered Data")
st.download_button(
    label="Download CSV",
    data=filtered_data.to_csv(index=False),
    file_name="filtered_cars_data.csv",
    mime="text/csv",
)

st.write("### Insights")
st.markdown("""
- The **Price vs Model Year** scatter plot shows that newer models tend to have higher prices.
- The **Count of Cars by Fuel Type** bar chart reveals the popularity of certain fuel types.
- The **Price Distribution by Condition** box plot indicates that cars in 'new' or 'excellent' condition typically have higher prices.
""")
