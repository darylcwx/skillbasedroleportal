from flask import Flask, Blueprint, jsonify, request
from backend.models.listings import Listings
from backend.routes.get.getStaffSkills import getStaffSkills
from backend.routes.get.getRoleSkills import getRoleSkills
from backend.routes.get.getApplicants import getApplicants
 
getAllRoleSkillMatchBP = Blueprint('getAllRoleSkillMatch', __name__)
@getAllRoleSkillMatchBP.route('/api/allroleskillmatch', methods=['GET'])
def getAllRoleSkillMatch(lid = None):
    try:
        if not lid:
            lid = request.args.get('lid')

        listing = Listings.query.filter_by(Listing_ID = lid).first() # check if valid listing

        if listing:
            applications = getApplicants(lid)[0].get_json()['Applicants']
            roleskills = getRoleSkills(listing.Role_Name)[0].get_json()['Role Skills']
            result = []

            for applicant in applications:
                print(applicant)
                staffskills = getStaffSkills(applicant['Staff_ID'])[0].get_json()['Staff Skills']

                matched_skills = []
                mismatched_skills = []
                percentage_match = 0.0 # if both role skills and staff skills are empty, also 0% match

                if roleskills and staffskills:
                    for skill in staffskills:
                        if skill in roleskills:
                            matched_skills.append(skill)

                        else:
                            mismatched_skills.append(skill)

                    percentage_match = str(round((len(matched_skills) / len(roleskills))*100, 2))

                result.append({'Application ID': applicant['Application_ID'],
                               'Staff Name': applicant['Name'],
                               'Staff Dept': applicant['Dept'],
                               'Staff Matched Skills': matched_skills,
                                'Staff Mismatched Skills': mismatched_skills,
                                'Percentage Match': percentage_match})
                
            return jsonify({'Applicants': result}), 200
        
        else:
            return jsonify({'error': 'Invalid role name. Role not found!'}), 404

         
    except Exception as error:
        return jsonify({'error': str(error)}), 500