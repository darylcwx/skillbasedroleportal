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
        missing_skills = []

        for skill in roleskills['Role Skills']:
            if skill in staffskills['Staff skills']:
                matched_skills.append(skill)

            else:
                missing_skills.append(skill)


        

        print(roleskills['Role Skills'])
        percentage_match = str(round((len(matched_skills) / len(roleskills['Role Skills']))*100, 2)) + '%'



        return jsonify({'Staff Matched Skills': matched_skills,
                        'Staff Missing Skills': missing_skills,
                        'Percentage Match': percentage_match}), 200

         
    except Exception as error:
        return jsonify({'error': str(error)}), 500