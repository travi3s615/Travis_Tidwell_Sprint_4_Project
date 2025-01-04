# Travis_Tidwell_Sprint_4_Project

## Project Description

This project demonstrates the development and deployment of a web application for analyzing and visualizing used car sales data. The app allows users to explore trends in vehicle prices, types, and other features through interactive charts and tables, utilizing **Streamlit**, **Plotly**, and **Pandas**. The goal is to enhance data analysis skills while mastering deployment to a cloud-based platform like Render.

You can view the live app here: [Travis Tidwell Sprint 4 Project](https://travis-tidwell-sprint-4-project.onrender.com/).

## Features

1. **Interactive Visualizations**:
   - Histograms and scatter plots for key variables like vehicle prices, model years, and more.
   - Bar charts highlighting trends such as fuel types and conditions.

2. **Data Preprocessing**:
   - Handling missing values for columns like `is_4wd`, `paint_color`, and `odometer`.
   - Duplicate removal and outlier identification.
   - Enrichment of data by breaking down complex attributes.

3. **Customization**:
   - Checkbox toggles for displaying additional plots and data insights.

## Installation Instructions

To run the app locally:

#### For Mac/Linux:
1. Clone the repository:
   ```bash
   git clone (https://github.com/travi3s615/Travis_Tidwell_Sprint_4_Project)
cd Travis_Tidwell_Sprint_4_Project

2. #### Set up a virtual enviorment:

python3 -m venv env
source env/bin/activate 

3. #### Install the required dependencies : 

pip install -r requirement.txt

4. #### Run the Streamlit app : 

streamlit run app.py

#### For Windows:

1. #### Clone the repository:

git clone (https://github.com/travi3s615/Travis_Tidwell_Sprint_4_Project)
cd Travis_Tidwell_Sprint_4_Project

2. #### Set up a virtual environment:

python -m venv env
.\env\Scripts\activate

3. #### Install the required dependencies:

pip install -r requirements.txt


4. Run the Streamlit app:

streamlit run app.py


## Project Structure for Locally

.
├── README.md
├── app.py
├── vehicles_us.csv
├── vehicles_us_cleaned.csv
├── requirements.txt
├── .streamlit
│   └── config.toml
├── notebooks
│   └── EDA.ipynb


