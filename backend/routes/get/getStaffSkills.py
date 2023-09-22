from flask import Flask, Blueprint, jsonify, request
from backend.models.staff import Staff
from backend.models.staffskills import StaffSkills
 
getStaffSkillsBP = Blueprint('getStaffSkills', __name__)
@getStaffSkillsBP.route('/api/staffskills', methods=['GET'])
def getStaffSkills(email):
    
    try:
        # email = request.args.get('email')
        user = Staff.query.filter_by(Email=email).first()
        if user:
            sid = user.Staff_ID
            skills = StaffSkills.query.filter_by(Staff_ID = sid).all()
            skill_list = [skill.serialize() for skill in skills]

            return jsonify({'Staff skills': skill_list}), 200
        
        else:
            return jsonify({'error': 'Invalid email. Staff not found!'}), 404

         
    except Exception as error:
        return jsonify({'error': str(error)}), 500