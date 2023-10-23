# run 'python load_empty_listings.py' to load the correct database for testing.
import mysql.connector
import os
from dotenv import load_dotenv
import subprocess

# Define the package name
package_name = 'mysql-connector-python'

# Check if the package is installed
try:
    import mysql.connector
    # print(f"{package_name} is already installed.")
except ImportError:
    # If the package is not installed, try to install it
    try:
        subprocess.check_call(['pip', 'install', package_name])
        print(f"{package_name} has been installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")


load_dotenv('backend/.env')

# Establish MySQL connection
user = os.getenv("DB_USER", "root")
password = os.getenv("DB_PASSWORD", "root")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT", 3306)
table_name = 'Listings'

db = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    port = port
)
cursor = db.cursor()

# # Read entire SQL file and execute with error checking
# with open('init.sql', 'r') as sql_file:
#     sql_as_string = sql_file.read()
#     sql_commands = sql_as_string.split(';')
#     for command in sql_commands:
#         try:
#             cursor.execute(command)
#         except:
#             print(f"Command skipped: {command}")

# remove all rows from Listings table
cursor.execute(f"use SBRP_Ais_Kachang")
cursor.execute(f"DELETE FROM {table_name}")

db.commit()

# Close cursor and connection
cursor.close()
db.close()
