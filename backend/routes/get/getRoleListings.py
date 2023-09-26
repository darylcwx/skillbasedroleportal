from flask import Blueprint, jsonify
from backend.models.listings import Listings
from backend.routes.get.getRoleDesc import getRoleDesc

getRoleListingsBP = Blueprint('getRoleListings', __name__)
# Get all listings
@getRoleListingsBP.route('/api/rolelistings', methods=['GET'])
def getRoleListings():
    try:
        rolelistings = Listings.query.all()
        lst = []

        for listing in rolelistings:
            roledesc = getRoleDesc(listing.Role_Name)[0].get_json()['Description']
            item = listing.serialize()
            item['Description'] = roledesc
            lst.append(item)

        if rolelistings:
            return jsonify({'Listings': lst}), 200
        else:
            return jsonify({'error': 'No listings found.'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500