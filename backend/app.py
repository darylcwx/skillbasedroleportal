from flask import Flask, Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend.config import db_uri

# Init flask instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
CORS(app)
db = SQLAlchemy(app)

# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
# db = SQLAlchemy(app)
 
# =================================================================
# Change connection details if required in models/connection.py
# =================================================================
# 1) Import and declare routes
from backend.routes.get.getUsers import getUsersBP
from backend.routes.get.getUser import getUserBP
from backend.routes.get.getStaffSkills import getStaffSkillsBP
from backend.routes.get.getRoleSkills import getRoleSkillsBP
from backend.routes.get.getRoleSkillMatch import getRoleSkillMatchBP

# 2) Register routes here
app.register_blueprint(getUsersBP)
app.register_blueprint(getUserBP)
app.register_blueprint(getStaffSkillsBP)
app.register_blueprint(getRoleSkillsBP)
app.register_blueprint(getRoleSkillMatchBP)



if __name__ == '__main__':
    app.run(debug=True)


