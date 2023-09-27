# run 'python load_init_sql.py' to load the full SBRP database.
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
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")

db = mysql.connector.connect(
    host = host,
    user = user,
    password = password
)

# Create cursor
cursor = db.cursor()

# Read entire SQL file and execute with error checking
with open('init.sql', 'r') as sql_file:
    sql_as_string = sql_file.read()
    sql_commands = sql_as_string.split(';')
    for command in sql_commands:
        try:
            cursor.execute(command)
        except:
            print(f"Command skipped: {command}")

# Close cursor and connection
cursor.close()
db.close()
