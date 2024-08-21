import psycopg2
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

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
