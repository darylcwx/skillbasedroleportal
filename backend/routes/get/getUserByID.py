from flask import Flask, Blueprint, jsonify, request
from backend.models.staff import Staff

getUserByIDBP = Blueprint('getUserByID', __name__)
@getUserByIDBP.route('/api/userID', methods=['GET'])
def getUserByID():
    try:
        id = request.args.get('id')
        user = Staff.query.filter_by(Staff_ID=id).first()
        if user:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({'error': 'User not found'}), 404
        
    except Exception as error:
        return jsonify({'error': str(error)}), 500
    