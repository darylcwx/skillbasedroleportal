from flask import Flask, Blueprint, jsonify, request
from backend.models.staff import Staff
from backend.models.staffskills import StaffSkills
 
getStaffSkillsBP = Blueprint('getStaffSkills', __name__)
@getStaffSkillsBP.route('/api/staffskills', methods=['GET'])
def getStaffSkills(sid = None):
     
    try:
        if not sid:
            sid = request.args.get('sid')

        # check valid staff ID
        user = Staff.query.filter_by(Staff_ID = sid).first()

        if user:
            skills = StaffSkills.query.filter_by(Staff_ID = sid).all()
            skill_list = [skill.Skill_Name for skill in skills]

            return jsonify({'Staff Skills': skill_list}), 200
        
        else:
            return jsonify({'error': 'Invalid staff ID. Staff not found!'}), 404

         
    except Exception as error:
        return jsonify({'error': str(error)}), 500