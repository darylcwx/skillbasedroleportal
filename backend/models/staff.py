from flask_sqlalchemy import SQLAlchemy
from backend.app import db

class Staff(db.Model):
    __tablename__ = 'Staff'

    Staff_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Dept = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False, unique=True)
    Access_Rights = db.Column(db.Integer, nullable=False)

    def __init__(self, Staff_FName, Staff_LName, Dept, Email, Access_Rights):
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Email = Email
        self.Access_Rights = Access_Rights

    def serialize(self):
        return {
            'Staff_ID': self.Staff_ID,
            'Staff_FName': self.Staff_FName,
            'Staff_LName': self.Staff_LName,
            'Dept': self.Dept,
            'Email': self.Email,
            'Access_Rights': self.Access_Rights
        }