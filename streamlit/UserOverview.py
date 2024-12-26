import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="User Overview Analysis", layout="wide")

# Title
st.title("User Overview Analysis")

# Load data
@st.cache
def load_data():
    return pd.read_csv('data/path_to_task1_results.csv')

data = load_data()

# Top 10 Handsets
st.write("### Top 10 Handsets")
handset_counts = data['Handset Type'].value_counts().head(10)
st.bar_chart(handset_counts)

# Top 3 Handset Manufacturers
st.write("### Top 3 Handset Manufacturers")
manufacturer_counts = data['Handset Manufacturer'].value_counts().head(3)
st.bar_chart(manufacturer_counts)

# Recommendations
st.write("### Recommendations")
st.write("- **Samsung** handsets dominate the market, followed by others.")
st.write("- Marketing efforts should prioritize high-usage handsets and brands.")