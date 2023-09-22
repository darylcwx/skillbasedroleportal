from flask import Flask, Blueprint, jsonify
from backend.models.staff import Staff

getUsersBP = Blueprint('getUsers', __name__)
@getUsersBP.route('/api/users', methods=['GET'])
def getUsers():
    try:
        users = Staff.query.all()
        user_list = [user.serialize() for user in users]
        return jsonify({'users': user_list}), 200
    
    except Exception as error:
        return jsonify({'error': str(error)}), 500