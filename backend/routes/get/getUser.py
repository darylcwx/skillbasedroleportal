from flask import Flask, Blueprint, jsonify, request
from backend.models.staff import Staff

getUserBP = Blueprint('getUser', __name__)
@getUserBP.route('/api/user', methods=['GET'])
def getUser():
    try:
        email = request.args.get('email')
        user = Staff.query.filter_by(Email=email).first()
        if user:
            return jsonify(user.serialize()), 200
        else:
            return jsonify({'error': 'User not found'}), 404
        
    except Exception as error:
        return jsonify({'error': str(error)}), 500