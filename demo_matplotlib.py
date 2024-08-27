import psycopg2
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

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

# Create a cursor object
cur = conn.cursor()

# Execute a query
cur.execute("SELECT date, value FROM sample_data ORDER BY date LIMIT 10")

# Fetch all rows
rows = cur.fetchall()

# Separate the data into two lists
dates = [row[0] for row in rows]
values = [row[1] for row in rows]

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(dates, values, marker='o')
plt.title('Data from Materialize')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Close the cursor and connection
cur.close()
conn.close()
