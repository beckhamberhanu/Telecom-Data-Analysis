import streamlit as st

# Page configuration
st.set_page_config(page_title="Telecom Dashboard", layout="wide")

# Title and Description
st.title("Telecom Data Analysis Dashboard")
st.write("""
Welcome to the Telecom Data Analysis Dashboard!  
Navigate through the analysis pages to explore insights:
- **User Overview Analysis**: Analyze top handsets, manufacturers, and insights.
- **User Engagement Analysis**: Explore customer engagement metrics.
- **User Experience Analysis**: Understand customer experience and QoS metrics.
""")

# Navigation Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Go to User Overview Analysis"):
        st.experimental_set_query_params(page="UserOverview")
        st.experimental_rerun()

with col2:
    if st.button("Go to User Engagement Analysis"):
        st.experimental_set_query_params(page="UserEngagement")
        st.experimental_rerun()

with col3:
    if st.button("Go to User Experience Analysis"):
        st.experimental_set_query_params(page="UserExperience")
        st.experimental_rerun()

# Footer
st.write("---")
st.write("Built with Streamlit | [GitHub Repository](https://github.com/YourGitHubRepo)")
