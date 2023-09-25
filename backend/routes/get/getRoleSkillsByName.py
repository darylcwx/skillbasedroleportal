from flask import Blueprint, jsonify, request
from backend.models.roleskills import RoleSkills

getRoleSkillsByNameBP = Blueprint('getRoleSkillsByName', __name__)
# Get role description by role name
@getRoleSkillsByNameBP.route('/api/roleskillsbyname', methods=['GET'])
def getRoleSkillsByName():
    args = request.args
    role_name = args.get('role_name')
    try:
        role_skills = RoleSkills.query.filter_by(Role_Name=role_name).all()
        if role_skills:
            return jsonify({'RoleSkills': [role_skill.serialize() for role_skill in role_skills]}), 200
        else:
            return jsonify({'error': 'No listings found.'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500
