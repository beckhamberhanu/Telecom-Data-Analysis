import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="User Experience Analysis", layout="wide")

# Title
st.title("User Experience Analysis")

# Load data
@st.cache
def load_data():
    return pd.read_csv('data/path_to_task3_results.csv')

data = load_data()

# Average Throughput by Handset Type
st.write("### Average Throughput by Handset Type")
avg_throughput = data.groupby('Handset Type')['Avg Bearer TP DL (kbps)'].mean().sort_values(ascending=False).head(10)
st.bar_chart(avg_throughput)

# TCP Retransmission Rates
st.write("### TCP Retransmission Rates")
tcp_retrans = data[['Handset Type', 'TCP DL Retrans. Vol (Bytes)']].sort_values(by='TCP DL Retrans. Vol (Bytes)', ascending=False).head(10)
st.table(tcp_retrans)

# Recommendations
st.write("### Recommendations")
st.write("- Optimize network performance for devices with higher retransmission rates.")
st.write("- Focus on high-usage handset types to improve the user experience.")
