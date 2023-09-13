from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

# Init flask instance
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# Establish MySQL connection
user='root'
password='password'
host='localhost'
port = 3306
db='SBRP'
connection = mysql.connector.connect(user=user, password=password, host=host, database=db)

# Routes 
@app.route('/api/roles', methods=['GET'])
def get_roles():
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM role"
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)
    except mysql.connector.Error as error:
        print("Error: ", error)

@app.route('/api/users', methods=['GET'])
def get_user():
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM user"
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)
    except mysql.connector.Error as error:
        print("Error: ", error)

if __name__ == '__main__':
    app.run(debug=True)
