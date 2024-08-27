import pandas as pd
import psycopg2
import plotly.express as px
import os

dsn = "user={} password={} host={} dbname={} port={} sslmode={} options='--cluster={} --search_path={}'".format(
    os.getenv('MZ_USER'),
    os.getenv('MZ_PASSWORD'),
    os.getenv('MZ_HOST'),
    os.getenv('MZ_DATABASE'),
    os.getenv('MZ_PORT', 6875),
    os.getenv('MZ_SSLMODE', 'require'),
    os.getenv('MZ_CLUSTER'),
    os.getenv('MZ_SCHEMA', 'public')
)

# Connect to Materialize
conn = psycopg2.connect(dsn)
conn.set_session(autocommit=True)

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
