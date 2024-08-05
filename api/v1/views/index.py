#!/usr/bin/python3
"""index module
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'])
def myStatus():
    """returns ok status message"""

    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def objStats():
    """retrieves agregated stats for all objs by class name"""

    stats = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User')
        }

    return jsonify(stats)
