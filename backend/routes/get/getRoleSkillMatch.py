from flask import Flask, Blueprint, jsonify, request
from backend.routes.get.getStaffSkills import getStaffSkills
from backend.routes.get.getRoleSkills import getRoleSkills
 
getRoleSkillMatchBP = Blueprint('getRoleSkillMatch', __name__)
@getRoleSkillMatchBP.route('/api/roleskillmatch', methods=['GET'])
def getRoleSkillMatch():
    try:
        email = request.args.get('email')
        role = request.args.get('role')
        # 'jude.smith@aio.com' 'IT Support'

        staffskills = getStaffSkills(email)[0].get_json() 
        roleskills = getRoleSkills(role)[0].get_json()

        matched_skills = []
        for skill in staffskills['Staff skills']:
            if skill['Skill_Name'] in roleskills['Role Skills']:
                matched_skills.append(skill)



        return jsonify({'Staff Matched Skills': matched_skills}), 200

         
    except Exception as error:
        return jsonify({'error': str(error)}), 500