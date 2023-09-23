# pip install mysql-connector-python;
import mysql.connector

# Establish MySQL connection
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
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
