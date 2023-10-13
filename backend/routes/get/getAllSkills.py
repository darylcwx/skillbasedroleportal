from flask import Flask, Blueprint, jsonify, request
from backend.models.skill import Skill
 
getAllSkillsBP = Blueprint('getAllSkills', __name__)
@getAllSkillsBP.route('/api/allskills', methods=['GET'])
def getAllSkills():
    try:
        skills = Skill.query.all()
        skill_list = [skill.serialize() for skill in skills]
        return jsonify({'skills': skill_list}), 200
    
    except Exception as error:
        return jsonify({'error': str(error)}), 500