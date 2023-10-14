from flask import Blueprint, jsonify, request
from backend.app import db
from backend.models.listings import Listings
from backend.models.role import Role

createRoleListingBP = Blueprint('createRoleListing', __name__)
@createRoleListingBP.route('/api/createRoleListing', methods=['POST'])
def createRoleListing():
    try:
        data = request.json
        # print(data)

        role = Role.query.get(data['name'])
        # print(role)
        
        if role:
            role.Role_Desc = data['desc']
            listing = Listings(None, data['name'], data['deadline'])
            db.session.add(listing)
            db.session.commit()

            return jsonify({
                    'Status': 'Role Listing created successfully.'
                }), 200
        
        else:
            return jsonify({
                    'Status': 'Rolename invalid. Not found.'
                }), 404
        

    except Exception as error:
        db.session.rollback()

        return jsonify({'error': str(error)}), 500