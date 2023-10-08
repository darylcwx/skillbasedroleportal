from flask import Blueprint, jsonify, request
from backend.app import db
from backend.models.listings import Listings
from backend.models.role import Role
from datetime import datetime

updateRoleListingBP = Blueprint('updateRoleListing', __name__)
@updateRoleListingBP.route('/api/updateRoleListing', methods=['POST'])
def updateRoleListing():
    try:
        data = request.json
        listing = Listings.query.get(data['lid'])
        role = Role.query.get(data['name'])
        
        if listing and role:
            listing.Deadline = data['deadline']
            role.Role_Desc = data['desc']
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