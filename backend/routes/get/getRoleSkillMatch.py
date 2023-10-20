from flask import Flask, Blueprint, jsonify, request
from backend.routes.get.getStaffSkills import getStaffSkills
from backend.routes.get.getRoleSkills import getRoleSkills
 
getRoleSkillMatchBP = Blueprint('getRoleSkillMatch', __name__)
@getRoleSkillMatchBP.route('/api/roleskillmatch', methods=['GET'])
def getRoleSkillMatch(sid = None, rolename = None):
    try:
        if not sid:
            sid = request.args.get('sid')

        if not rolename:
            rolename = request.args.get('rolename')

        staffskills = getStaffSkills(sid)[0].get_json() 
        roleskills = getRoleSkills(rolename)[0].get_json()

        matched_skills = []
        missing_skills = []
        percentage_match = 0.0

        if roleskills['Role Skills']:
            for skill in roleskills['Role Skills']:
                if skill in staffskills['Staff Skills']:
                    matched_skills.append(skill)

                else:
                    missing_skills.append(skill)

            percentage_match = str(round((len(matched_skills) / len(roleskills['Role Skills']))*100, 2))

        return jsonify({'Staff Matched Skills': matched_skills,
                        'Staff Missing Skills': missing_skills,
                        'Percentage Match': percentage_match}), 200
        

    except Exception as error:
        return jsonify({'error': str(error)}), 500