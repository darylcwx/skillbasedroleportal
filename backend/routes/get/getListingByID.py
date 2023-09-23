from flask import Blueprint, jsonify
from backend.models.listings import Listings

getListingsBP = Blueprint('getListings', __name__)
# Get listing by ID
@getListingsBP.route('/api/listings/<int:id>', methods=['GET'])
def getListingByID(id):
    try:
        listing = Listings.query.get(id)
        if listing:
            return jsonify({'Listing': listing.serialize()}), 200
        else:
            return jsonify({'error': 'Listing not found.'}), 404

    except Exception as error:
        return jsonify({'error': str(error)}), 500
