from flask import Blueprint, jsonify
from backend.app import db
from backend.models.listings import Listings
from backend.models.staff import Staff
from backend.models.staffapplication import StaffApplication


updateStaffApplicationBP = Blueprint("updateStaffApplication", __name__)
@updateStaffApplicationBP.route("/api/updateStaffApplication/<listingID>/<staffID>", methods=["POST"])
def updateStaffApplication(staffID, listingID):
    try:
        staff = Staff.query.get(staffID)
        listing = Listings.query.get(listingID)

        if staff and listing:
            staff_application = StaffApplication.query.filter_by(
                Staff_ID=staffID, Listing_ID=listingID
            ).first()
            if staff_application:
                return (
                    jsonify(
                        {"Status": "Staff and Listing combination already exists."}
                    ),
                    400,
                )
            else:
                staff_application = StaffApplication(Staff_ID = staffID, Listing_ID = listingID)
                db.session.add(staff_application)

                db.session.commit()

                return jsonify({"Status": "Data updated successfully."}), 200

        else:
            return (
                jsonify({"Status": "ListingID or StaffID invalid. Not found."}),
                404,
            )

    except Exception as error:
        db.session.rollback()

        return jsonify({"error": str(error)}), 500
