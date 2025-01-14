import streamlit as st
import pandas as pd
import plotly.express as px

#Title of the app
st.title("My Streamlit App")

#Load the dataset
df = pd.read_csv('vehicles_us.csv')

#Add a header
st.header("Vehicle Sales Dashboard")

#Create a Histogram with unique parameters
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist, key='unique_histogram_key_1')  # Add a unique key

#Create a Scatter Plot with unique parameters
fig_scatter = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_scatter, key='unique_scatter_key_2')  # Add a unique key

#Add a Checkbox with a unique key
if st.checkbox('Show raw data', key='raw_data_checkbox'):
    st.write(df)
