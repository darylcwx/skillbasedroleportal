from backend.app import db
from role import Role

class Listings(db.Model):
    __tablename__ = 'Listings'

    Listing_ID = db.Column(db.INTEGER, primary_key=True, nullable=False)
    Role_Name = db.Column(db.VARCHAR(20), db.ForeignKey(Role.Role_Name), nullable=False)
    Deadline = db.Column(db.DATE, nullable=False)

    def __init__(self, Listing_ID, Role_Name, Deadline):
        self.Listing_ID = Listing_ID
        self.Role_Name = Role_Name
        self.Deadline = Deadline

    def serialize(self):
        return {
            'Listing_ID': self.Listing_ID,
            'Role_Name': self.Role_Name,
            'Deadline': self.Deadline
        }