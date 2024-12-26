import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="User Engagement Analysis", layout="wide")

# Title
st.title("User Engagement Analysis")

# Load data
@st.cache
def load_data():
    return pd.read_csv('data/path_to_task2_results.csv')

data = load_data()

# Top 10 Customers by Engagement Metrics
st.write("### Top 10 Customers by Engagement")
top_customers = data[['MSISDN/Number', 'Engagement Score']].sort_values(by='Engagement Score', ascending=False).head(10)
st.table(top_customers)

# K-Means Clustering
st.write("### Engagement Clusters")
sns.countplot(x=data['Engagement Cluster'])
st.pyplot(plt)

# Recommendations
st.write("### Recommendations")
st.write("- **High-engagement clusters** should be prioritized for better service.")
st.write("- Optimize resources for top-used applications.")
