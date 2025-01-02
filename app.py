import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('vehicles_us.csv')

# Ensure the 'price' column is numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Drop rows with missing or invalid 'price' values
df = df.dropna(subset=['price'])

# Convert 'price' to integers for consistency (optional)
df['price'] = df['price'].astype(int)

# Display the dataset
st.dataframe(df.head(51))

# Sidebar Filters
st.sidebar.header("Filter Options")

# Dropdown for selecting fuel type
fuel_type = st.sidebar.selectbox("Select Fuel Type", options=df['fuel'].unique())

# Slider for price range
min_price, max_price = st.sidebar.slider(
    "Select Price Range", int(df['price'].min()), int(df['price'].max()), (5000, 20000)
)

# Filter the data
filtered_data = df[(df['fuel'] == fuel_type) & (df['price'] >= min_price) & (df['price'] <= max_price)]

# Check if data exists
if filtered_data.empty:
    st.warning("No data matches the selected filters.")
else:
    # Scatter Plot for Price vs Model Year
    st.write("### Price vs Model Year (Filtered)")
    scatter = px.scatter(
        filtered_data, x='model_year', y='price', title='Price vs Model Year (Filtered)'
    )
    st.plotly_chart(scatter)

    # Bar Chart for Fuel Type Count
    st.write("### Count of Cars by Fuel Type")
    bar_chart = px.bar(df, x='fuel', title='Count of Cars by Fuel Type', color='fuel')
    st.plotly_chart(bar_chart)

    # Box Plot for Price Distribution by Condition
    st.write("### Price Distribution by Condition")
    box_plot = px.box(
        df, x='condition', y='price', color='condition', title='Price Distribution by Condition'
    )
    st.plotly_chart(box_plot)

# Show Raw Data Checkbox
if st.checkbox("Show Raw Data"):
    st.write(df)

# Download Button for Filtered Data
st.write("### Download Filtered Data")
st.download_button(
    label="Download CSV",
    data=filtered_data.to_csv(index=False),
    file_name="filtered_cars_data.csv",
    mime="text/csv",
)

# Insights Section
st.write("### Insights")
st.markdown("""
- The **Price vs Model Year** scatter plot shows that newer models tend to have higher prices.
- The **Count of Cars by Fuel Type** bar chart reveals the popularity of certain fuel types.
- The **Price Distribution by Condition** box plot indicates that cars in 'new' or 'excellent' condition typically have higher prices.
""")

