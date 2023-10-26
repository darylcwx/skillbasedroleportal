from flask import Blueprint, jsonify, request
from backend.app import db
from backend.models.listings import Listings
from backend.models.role import Role
from backend.routes.get.getAvailableRoles import getAvailableRoles
from datetime import datetime

createRoleListingBP = Blueprint('createRoleListing', __name__)
@createRoleListingBP.route('/api/createRoleListing', methods=['POST'])
def createRoleListing():
    try:
        data = request.json
        availableRoles = getAvailableRoles()[0].get_json()['roles']
        avail = False

        for role in availableRoles:
            if role["Role_Name"] == data['name']:
                avail = True
                break

        if avail:
            if (data['deadline'] > datetime.now().strftime('%Y-%m-%d')) or (data['deadline'] == datetime.now().strftime('%Y-%m-%d') and datetime.now().strftime('%H:%M:%S') < '23:59:00'):
                role = Role.query.get(data['name'])

                if role:
                    role.Role_Desc = data['desc']
                    listing = Listings(Role_Name = data['name'], Deadline = data['deadline'])
                    db.session.add(listing)
                    db.session.commit()

                    return jsonify({
                            'Status': 'Role Listing created successfully.'
                        }), 200
                
                else:
                    return jsonify({
                            'Status': 'Rolename invalid. Not found.'
                        }), 404
            
            else:
                return jsonify({
                        'Status': 'Invalid deadline. Date has passed.'
                    }), 404
            
        else:
            return jsonify({
                'Status': 'Unavailable Role. There is an existing role listing open.'
            }), 404
        

    except Exception as error:
        db.session.rollback()
        return jsonify({'error': str(error)}), 500