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

st.markdown("""
### Loading and Cleaning the Dataset
- The dataset `vehicles_us.csv` is loaded into a Pandas DataFrame.
- The `price` column is converted to numeric, and invalid values are coerced to `NaN`.
- Rows with missing or invalid `price` values are removed.
- The `price` column is converted to integers for consistency.
- The `model_year` column is also converted to numeric, invalid values are removed, and the column is converted to integers.
""")

if st.checkbox("Show Raw Data"):
    st.write("### Raw Data")
    st.dataframe(df.head(51))

    st.markdown("""
    - This command displays the first 51 rows of the cleaned DataFrame to verify that the data is loaded and cleaned correctly.
    """)

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

    st.markdown("""
    - A scatter plot visualizes the relationship between `model_year` (x-axis) and `price` (y-axis).
    - Labels and titles are added for clarity. This visualization helps identify trends, such as newer cars generally having higher prices.
    """)

    st.write("### Count of Cars by Fuel Type")
    fuel_type_data = filtered_data.groupby('fuel').size().reset_index(name='count')
    bar_chart = px.bar(
        fuel_type_data,
        x='fuel',
        y='count',
        title='Count of Cars by Fuel Type',
        labels={'fuel': 'Fuel Type', 'count': 'Count'},
        color='fuel',
    )
    st.plotly_chart(bar_chart)

    st.markdown("""
    - A bar chart is created to show the number of cars for each fuel type in the dataset.
    - The `color` parameter ensures that each fuel type is displayed in a unique color, improving readability.
    """)

    st.write("### Price Distribution by Condition")
    box_plot = px.box(
        filtered_data,
        x='condition',
        y='price',
        title='Price Distribution by Condition',
        labels={'condition': 'Condition', 'price': 'Price ($)'},
        color='condition',
    )
    st.plotly_chart(box_plot)

    st.markdown("""
    - A box plot is created to analyze the distribution of prices across different vehicle conditions (e.g., `excellent`, `good`, `fair`).
    - The `color` parameter highlights each condition category with a distinct color. This plot helps identify variations in pricing based on vehicle condition.
    """)

    st.write("### Download Filtered Data")
    st.download_button(
        label="Download Filtered Data as CSV",
        data=filtered_data.to_csv(index=False),
        file_name='filtered_vehicles_data.csv',
        mime='text/csv'
    )

    st.markdown("""
    - A download button allows users to save the filtered dataset as a CSV file for further analysis.
    """)

    st.write("### Insights")
    st.markdown("""
    - The **Price vs Model Year** scatter plot shows that newer vehicles generally have higher prices.
    - The **Count of Cars by Fuel Type** bar chart highlights the distribution of vehicles by fuel type.
    - The **Price Distribution by Condition** box plot indicates that vehicles in better condition tend to be priced higher.
    """)
