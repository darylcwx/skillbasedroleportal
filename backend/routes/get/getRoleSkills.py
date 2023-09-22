from flask import Flask, Blueprint, jsonify, request
from backend.models.roleskills import RoleSkills
 
getRoleSkillsBP = Blueprint('getRoleSkills', __name__)
@getRoleSkillsBP.route('/api/roleskills', methods=['GET'])
def getRoleSkills(role):
    try:
        # role = request.args.get('role')
        if role:
            roleskills = RoleSkills.query.filter_by(Role_Name=role).all()
            skill_list = [skills.Skill_Name for skills in roleskills]

            return jsonify({'Role Skills': skill_list}), 200
        
        else:
            return jsonify({'error': 'Invalid role name.'}), 404

        
    except Exception as error:
        return jsonify({'error': str(error)}), 500