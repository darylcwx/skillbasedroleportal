from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend.config import db_uri

# Init flask instance
app = Flask(__name__)
cors = CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db = SQLAlchemy(app)

# =================================================================
# Change connection details if required in models/connection.py
# =================================================================
# 1) Import and declare routes
from backend.routes.get.getUsers import getUsersBP
from backend.routes.get.getUser import getUserBP

# 2) Register routes here
app.register_blueprint(getUsersBP)
app.register_blueprint(getUserBP)


if __name__ == '__main__':
    app.run(debug=True)


