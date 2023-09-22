from flask_sqlalchemy import SQLAlchemy
from backend.app import db

class RoleSkills(db.Model):
    __tablename__ = 'Role_Skill'
 
    Role_Name = db.Column(db.String(50), primary_key=True, nullable=False)
    Skill_Name = db.Column(db.String(50), nullable=False)

    def __init__(self, Role_Name, Skill_Name):
        self.Role_Name = Role_Name
        self.Skill_Name = Skill_Name

    def serialize(self):
        return {
            'Role_Name': self.Role_Name,
            'Skill_Name': self.Skill_Name
        }