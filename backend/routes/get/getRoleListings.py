from flask import Blueprint, jsonify
from backend.models.listings import Listings

getRoleListingsBP = Blueprint('getRoleListings', __name__)
# Get all listings
@getRoleListingsBP.route('/api/rolelistings', methods=['GET'])
def getRoleListings():
    try:
        rolelistings = Listings.query.all()
        if rolelistings:
            return jsonify({'Listings': [rolelisting.serialize() for rolelisting in rolelistings]}), 200
        else:
            return jsonify({'error': 'No listings found.'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500
