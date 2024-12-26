import streamlit as st

st.set_page_config(
    page_title="Telecom Data Analysis",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Telecom Data Analysis Dashboard")
st.sidebar.success("Select a page above.")

st.markdown("""
### Welcome to the Telecom Data Analysis Dashboard

This dashboard provides comprehensive insights into telecom user data across multiple dimensions:

#### 📊 Available Analysis Pages:

1. **User Overview Analysis**
   - Basic user statistics
   - Demographics
   - User status distribution

2. **User Engagement Analysis**
   - Usage patterns
   - Activity metrics
   - Engagement trends

3. **Experience Analysis**
   - Service quality metrics
   - Network performance
   - Technical indicators

4. **Satisfaction Analysis**
   - Customer satisfaction scores
   - Feedback analysis
   - Retention metrics

Please select a page from the sidebar to explore detailed analysis in each area.
""")