from flask_sqlalchemy import SQLAlchemy
from backend.app import db

class Staff(db.Model):
    __tablename__ = 'Staff'

    Staff_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Dept = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.Text, nullable=False)
    Email = db.Column(db.String(50), nullable=False, unique=True)
    Role = db.Column(db.Integer, nullable=False)

    def __init__(self, Staff_ID, Staff_FName, Staff_LName, Dept, Country, Email, Role):
        self.Staff_ID = Staff_ID,
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Country = Country
        self.Email = Email
        self.Role = Role

    def serialize(self):
        return {
            'Staff_ID': self.Staff_ID,
            'Staff_FName': self.Staff_FName,
            'Staff_LName': self.Staff_LName,
            'Dept': self.Dept,
            'Country': self.Country, 
            'Email': self.Email,
            'Role': self.Role
        }