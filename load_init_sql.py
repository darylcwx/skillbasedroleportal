# run 'python load_init_sql.py' to load the full SBRP database.
import sqlite3
import mysql.connector
import os
import csv
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

db = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    port = port
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
        except Exception as e:
            print(f"Command skipped: {command}")
            print(e)

# populate database with client provided data in CSV files
# specify the path to the folder containing the CSV files
folder_path = "./scheduler_data"

placeholders = ""

folder = ["access_control.csv", "staff.csv", "role.csv", "skill.csv", "role_skill.csv", "staff_skill.csv", "listings.csv", "staff_application.csv"]

# iterate through all files in the folder
for file_name in folder:
    print("Loading data from", file_name, "into database.")
    # check if the file is a CSV file
    if file_name.endswith(".csv"):
        # open the file
        # with open(os.path.join(folder_path, file_name), 'r') as csv_file:
        print(os.listdir())
        with open(os.path.join(folder_path, file_name), encoding="ISO-8859-1") as csv_file:
            # create a CSV reader object
            csv_reader = csv.reader(csv_file)
            # skip the header row
            next(csv_reader)

            # loop through the rows in the CSV file
            for row in csv_reader:
                # check if the row is not empty
                if row:
                    values = []
                    for item in row:
                        # check if the item is a string
                        if isinstance(item, str):
                            # add quotes around the item
                            values.append(f'"{item}"')
                        else:
                            # add the item as is
                            values.append(item)
                    # create a string of placeholders for the SQL string
                    placeholders = ','.join(values)

                    # special table staff_skill - to append with a NULL column.
                    if file_name[:-4] == "staff_skill":
                        placeholders += ",NULL"

                    # create the SQL string
                    sql_string = f"INSERT INTO {file_name[:-4]} VALUES ({placeholders});"
                    # execute the SQL string
                    try:
                        cursor.execute(sql_string)
                    except sqlite3.Error as e:
                        print(f"Error inserting data into {file_name[:-4]}: {placeholders}")
            print(f"{file_name} data loaded successfully.\n")

# Close cursor and connection
db.commit()
cursor.close()
db.close()
