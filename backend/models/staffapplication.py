from backend.app import db


class StaffApplication(db.Model):
    __tablename__ = "Staff_Application"

    Application_ID = db.Column(db.Integer, primary_key=True, nullable=False)
    Staff_ID = db.Column(db.Integer, nullable=False)
    Listing_ID = db.Column(db.Integer, nullable=False)

    def __init__(self, Staff_ID, Listing_ID):
        self.Staff_ID = Staff_ID
        self.Listing_ID = Listing_ID

    def serialize(self):
        return {
            "Application_ID": self.Application_ID,
            "Staff_ID": self.Staff_ID,
            "Listing_ID": self.Listing_ID,
        }
