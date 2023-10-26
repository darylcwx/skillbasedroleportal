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
# Change connection details if required in config.py
# =================================================================
# 1) Import and declare routes
from backend.routes.get.getUsers import getUsersBP
from backend.routes.get.getUser import getUserBP
from backend.routes.get.getUserByID import getUserByIDBP
from backend.routes.get.getAllRoleSkillMatch import getAllRoleSkillMatchBP
from backend.routes.get.getStaffSkills import getStaffSkillsBP
from backend.routes.get.getRoleSkills import getRoleSkillsBP
from backend.routes.get.getRoleSkillMatch import getRoleSkillMatchBP
from backend.routes.get.getRoleListings import getRoleListingsBP
from backend.routes.get.getRoleDesc import getRoleDescBP
from backend.routes.get.getApplicants import getApplicantsBP
from backend.routes.get.getAllSkills import getAllSkillsBP
from backend.routes.get.getRoles import getRolesBP

from backend.routes.post.updateRoleListing import updateRoleListingBP
from backend.routes.post.createRoleListing import createRoleListingBP
from backend.routes.post.updateStaffApplication import updateStaffApplicationBP

# 2) Register routes here
app.register_blueprint(getUsersBP)
app.register_blueprint(getUserBP)
app.register_blueprint(getUserByIDBP)
app.register_blueprint(getAllRoleSkillMatchBP)
app.register_blueprint(getStaffSkillsBP)
app.register_blueprint(getRoleSkillsBP)
app.register_blueprint(getRoleSkillMatchBP)
app.register_blueprint(getRoleListingsBP)
app.register_blueprint(getRoleDescBP)
app.register_blueprint(getApplicantsBP)
app.register_blueprint(getAllSkillsBP)
app.register_blueprint(getRolesBP)

app.register_blueprint(updateRoleListingBP)
app.register_blueprint(createRoleListingBP)
app.register_blueprint(updateStaffApplicationBP)


if __name__ == "__main__":
    app.run(debug=True)
