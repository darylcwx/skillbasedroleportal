from flask import Blueprint, jsonify
from backend.models.listings import Listings

getListingsBP = Blueprint('getListings', __name__)
# Get all listings
@getListingsBP.route('/api/listings', methods=['GET'])
def getListings():
    try:
        listings = Listings.query.all()
        if listings:
            return jsonify({'Listings': [listing.serialize() for listing in listings]}), 200
        else:
            return jsonify({'error': 'No listings found.'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500
