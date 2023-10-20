from flask import Blueprint, jsonify, request
from datetime import datetime, date
from backend.models.listings import Listings
from backend.routes.get.getRoleDesc import getRoleDesc
from backend.routes.get.getRoleSkillMatch import getRoleSkillMatch

getRoleListingsBP = Blueprint('getRoleListings', __name__)
@getRoleListingsBP.route('/api/rolelistings', methods=['GET'])
def getRoleListings(sid = None):
    try:
        if not sid:
            sid = request.args.get('staff_ID')

        rolelistings = Listings.query.order_by('Deadline').all()
        lst = []
        exp_lst = []

        for listing in rolelistings:
            roledesc = getRoleDesc(listing.Role_Name)[0].get_json()['Description']
            rsm = getRoleSkillMatch(sid, listing.Role_Name)[0].get_json()

            item = listing.serialize()
            item['Description'] = roledesc
            item['Staff Matched Skills'] = rsm['Staff Matched Skills']
            item['Staff Missing Skills'] = rsm['Staff Missing Skills']
            item['Percentage Match'] = rsm['Percentage Match']

            if (item['Deadline'] > date.today()) or (item['Deadline'] == date.today() and datetime.now().strftime('%H:%M:%S') < '23:59:59'):
                lst.append(item)

            else:
                exp_lst = [item] + exp_lst   

        lst = sorted(lst, key=lambda x: x['Percentage Match'], reverse=True)
        lst += exp_lst

        if rolelistings:
            return jsonify({'Listings': lst}), 200
        
        else:
            return jsonify({'error': 'No listings found.'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500