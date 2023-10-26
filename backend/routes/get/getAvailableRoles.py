from flask import Blueprint, jsonify
from backend.models.listings import Listings
from backend.routes.get.getRoles import getRoles
from backend.routes.get.getRoleDesc import getRoleDesc
from backend.routes.get.getRoleListings import getRoleListings
from datetime import datetime

getAvailableRolesBP = Blueprint('getAvailableRoles', __name__)
@getAvailableRolesBP.route('/api/availableroles', methods=['GET'])
def getAvailableRoles():
    try:
        roles = getRoles()[0].get_json()['roles']
        rolelistings = Listings.query.all()

        if roles and rolelistings:
            dic = {}
            lst = [] # list of available roles

            current_date = datetime.now().date()

            for listing in rolelistings:
                if listing.Role_Name not in dic:
                    dic[listing.Role_Name] = getRoleDesc(listing.Role_Name)[0].get_json()['Description']

                if listing.Deadline >= current_date: # already have open listings 
                    dic[listing.Role_Name] = None

            for key, value in dic.items():
                if value:
                    lst.append({"Role_Name": key, "Role_Desc": value})

            for role in roles:
                if role["Role_Name"] not in dic:
                    lst.append(role)


            return jsonify({'roles': lst}), 200
        
        else:
            return jsonify({'error': 'Couldnt retrieve roles and/or rolelistings'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500