import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration using environment variables
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'telecom_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
}

def load_table_to_dataframe(table_name):
    """Connect to PostgreSQL and load table into a DataFrame."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error loading table {table_name}: {e}")
        return None

if __name__ == "__main__":
    # Load tables as needed
    users_data = load_table_to_dataframe("users")
    xdr_data = load_table_to_dataframe("xdr_sessions")
    print(users_data.head())
    print(xdr_data.head())