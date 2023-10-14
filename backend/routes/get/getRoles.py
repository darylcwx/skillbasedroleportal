from flask import Flask, Blueprint, jsonify
from backend.models.role import Role
 
getRolesBP = Blueprint('getRoles', __name__)
@getRolesBP.route('/api/roles', methods=['GET'])
def getRoles():
    try:
        roles = Role.query.all()
        role_list = [role.serialize() for role in roles]
        return jsonify({'roles': role_list}), 200
    
    except Exception as error:
        return jsonify({'error': str(error)}), 500