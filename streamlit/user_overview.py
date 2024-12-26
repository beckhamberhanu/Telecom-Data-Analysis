import pandas as pd
import plotly.express as px
from scripts.load_data import load_table_to_dataframe

st.set_page_config(page_title="User Overview", page_icon="👥", layout="wide")

st.title("👥 User Overview Analysis")

# Load data
users_df = load_table_to_dataframe("users")

if users_df is not None:
    # Display basic statistics
    st.header("Key Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Users", len(users_df))
    with col2:
        st.metric("Active Users", len(users_df[users_df['status'] == 'active']))
    with col3:
        st.metric("Inactive Users", len(users_df[users_df['status'] == 'inactive']))

    # Create two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        # User Status Distribution
        st.subheader("User Status Distribution")
        status_counts = users_df['status'].value_counts()
        fig_status = px.pie(values=status_counts.values, 
                           names=status_counts.index, 
                           title="User Status Distribution")
        st.plotly_chart(fig_status, use_container_width=True)

        # User Type Distribution
        st.subheader("User Type Distribution")
        type_counts = users_df['user_type'].value_counts()
        fig_type = px.bar(x=type_counts.index, 
                         y=type_counts.values,
                         title="Distribution of User Types")
        fig_type.update_layout(xaxis_title="User Type", 
                             yaxis_title="Count")
        st.plotly_chart(fig_type, use_container_width=True)

    with col2:
        # Age Distribution
        st.subheader("Age Distribution")
        fig_age = px.histogram(users_df, 
                             x='age', 
                             nbins=30,
                             title="Age Distribution of Users")
        st.plotly_chart(fig_age, use_container_width=True)

    # Add filters in sidebar
    st.sidebar.header("Filters")
    status_filter = st.sidebar.multiselect(
        "Select Status:",
        options=users_df['status'].unique(),
        default=users_df['status'].unique()
    )

    # Show filtered raw data
    if st.checkbox("Show Raw Data"):
        st.subheader("Raw Data")
        filtered_df = users_df[users_df['status'].isin(status_filter)]
        st.dataframe(filtered_df)
else:
    st.error("Failed to load user data. Please check your database connection.")