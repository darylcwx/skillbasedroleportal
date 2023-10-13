from backend.app import db
from sqlalchemy.dialects.mysql import LONGTEXT

class Skill(db.Model):
    __tablename__ = 'Skill'

    Skill_Name = db.Column(db.VARCHAR(20), primary_key=True, nullable=False)
    Skill_Desc = db.Column(LONGTEXT, nullable=False)

    def __init__(self, Skill_Name, Skill_Desc):
        self.Skill_Name = Skill_Name
        self.Skill_Desc = Skill_Desc

    def serialize(self):
        return {
            'Role_Name': self.Skill_Name,
            'Role_Desc': self.Skill_Desc
        }