from flask_sqlalchemy import SQLAlchemy
from backend.app import db

class StaffSkills(db.Model):
    __tablename__ = 'Staff_Skill'
 
    Staff_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Skill_Name = db.Column(db.String(50), primary_key=True, nullable=False)
    Skill_Profile_Desc = db.Column(db.String(50), nullable=False)

    def __init__(self, Skill_Name, Skill_Profile_Desc):
        self.Skill_Name = Skill_Name
        self.Skill_Profile_Desc = Skill_Profile_Desc

    def serialize(self):
        return {
            'Staff_ID': self.Staff_ID,
            'Skill_Name': self.Skill_Name,
            'Skill_Profile_Desc': self.Skill_Profile_Desc
        }