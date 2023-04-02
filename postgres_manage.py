import psycopg2
from dotenv import load_dotenv
import os

# Retrive the env variable for DB connection
load_dotenv('./postgres.env')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASS = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

# Create the connection to PostGRES DB
conn = psycopg2.connect(
    database=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASS,
    host='127.0.0.1',
    port=5432
)

# Enable autocommit
conn.autocommit = True

# Create a curson for next query
cursor = conn.cursor()

# Execute the query
cursor.execute('''SELECT * from MOVIES''')

# Store the query results
result = cursor.fetchall()

# Close the connection with DB
conn.close()




