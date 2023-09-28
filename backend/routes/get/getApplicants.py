from flask import Flask, Blueprint, jsonify, request
from backend.models.staffapplication import StaffApplication
from backend.models.staff import Staff
 
getApplicantsBP = Blueprint('getApplicants', __name__)
@getApplicantsBP.route('/api/applicants', methods=['GET'])
def getApplicants(lid = None):
    try:
        if not lid:
            lid = request.args.get('lid')

        applications = StaffApplication.query.filter_by(Listing_ID = lid).all()
        result = []

        for applicant in applications:
            staff = Staff.query.filter_by(Staff_ID = applicant.Staff_ID).first()
            staff_name = staff.Staff_FName + ' ' + staff.Staff_LName

            result.append({'Application_ID': applicant.Application_ID,
                            'Staff_ID': staff.Staff_ID,
                            'Name': staff_name,
                            'Dept': staff.Dept,
                            'Email': staff.Email})
            
        return jsonify({'Applicants': result}), 200
         
    except Exception as error:
        return jsonify({'error': str(error)}), 500