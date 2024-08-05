#!/usr/bin/python3
"""index module
"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def myStatus():
    """returns ok status message"""

    return jsonify({"status": "OK"})
