from flask import Blueprint, jsonify
from backend.app import db
from backend.models.listings import Listings
from backend.models.role import Role

updateRoleListingBP = Blueprint('updateRoleListing', __name__)
@updateRoleListingBP.route('/api/updateRoleListing', methods=['POST'])
def updateRoleListing(lid, name, desc, deadline):
    try:
        listing = Listings.query.get(lid)
        role = Role.query.get(name)
        
        if listing and role:
            listing.Deadline = deadline
            role.Role_Desc = desc
            db.session.commit()

            return jsonify({
                    'Status': 'Data updated successfully.'
                }), 200
        
        else:
            return jsonify({
                    'Status': 'Rolename or Listing ID invalid. Not found.'
                }), 404
        

    except Exception as error:
        db.session.rollback()

        return jsonify({'error': str(error)}), 500