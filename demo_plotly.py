import pandas as pd
import psycopg2
import plotly.express as px

# Materialize connection details
MZ_HOST = os.getenv('MZ_HOST')
MZ_PORT = os.getenv('MZ_PORT')
MZ_USER = os.getenv('MZ_USER')
MZ_PASSWORD = os.getenv('MZ_PASSWORD')
MZ_DATABASE = os.getenv('MZ_DATABASE')

# Connect to Materialize
conn = psycopg2.connect(
    host=MZ_HOST,
    port=MZ_PORT,
    user=MZ_USER,
    password=MZ_PASSWORD,
    database=MZ_DATABASE
)

# SQL query to fetch data from the view
query = "SELECT * FROM sample_data_view"

# Load data into DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print DataFrame to verify
print(df)

# Plot using Plotly - line chart of 'value' over 'date'
fig = px.line(df, x='date', y='value', title='Value Over Time')
fig.show()
