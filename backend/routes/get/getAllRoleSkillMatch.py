from flask import Flask, Blueprint, jsonify, request
from backend.models.listings import Listings
from backend.models.staffapplication import StaffApplication
from backend.routes.get.getStaffSkills import getStaffSkills
from backend.routes.get.getRoleSkills import getRoleSkills
 
getAllRoleSkillMatchBP = Blueprint('getAllRoleSkillMatch', __name__)
@getAllRoleSkillMatchBP.route('/api/allroleskillmatch', methods=['GET'])
def getAllRoleSkillMatch(lid = None):
    # HR 
    # get the role skill match of each applicant for a given role name
    try:
        if not lid:
            lid = request.args.get('lid')

        listing = Listings.query.filter_by(Listing_ID = lid).first() # check if valid listing

        if listing:
            applications = StaffApplication.query.filter_by(Listing_ID = lid).all()
            roleskills = getRoleSkills(listing.Role_Name)[0].get_json()['Role Skills']
            result = []

            for applicant in applications:
                staffskills = getStaffSkills(applicant.Staff_ID)[0].get_json()['Staff Skills']

                matched_skills = []
                missing_skills = []
                percentage_match = 0.0 # if both role skills and staff skills are empty, also 0% match

                if roleskills and staffskills:
                    for skill in roleskills:
                        if skill in staffskills:
                            matched_skills.append(skill)

                        else:
                            missing_skills.append(skill)

                    percentage_match = str(round((len(matched_skills) / len(roleskills))*100, 2)) + '%'

                result.append({'Application_ID': applicant.Application_ID,
                               'Staff_ID': applicant.Staff_ID,
                               'Staff Matched Skills': matched_skills,
                                'Staff Missing Skills': missing_skills,
                                'Percentage Match': percentage_match})
                
            return jsonify({'Applicants': result}), 200
        
        else:
            return jsonify({'error': 'Invalid role name. Role not found!'}), 404

         
    except Exception as error:
        return jsonify({'error': str(error)}), 500