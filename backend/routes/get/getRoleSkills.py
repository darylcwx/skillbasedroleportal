from flask import Flask, Blueprint, jsonify, request
from backend.models.role import Role
from backend.models.roleskills import RoleSkills
 
getRoleSkillsBP = Blueprint('getRoleSkills', __name__)
@getRoleSkillsBP.route('/api/roleskills', methods=['GET'])
def getRoleSkills(rolename = None):
    try: 
        if not rolename:
            rolename = request.args.get('rolename')
            
        role = Role.query.filter_by(Role_Name = rolename).first() # check if valid role

        if role:
            roleskills = RoleSkills.query.filter_by(Role_Name = rolename).all()
            skill_list = [skills.Skill_Name for skills in roleskills]

            return jsonify({'Role Skills': skill_list}), 200
        
        else:
            return jsonify({'error': 'Invalid role name. Role not found!'}), 404

        
    except Exception as error:
        return jsonify({'error': str(error)}), 500