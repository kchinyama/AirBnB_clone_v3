#!/usr/bin/python3
"""script to manage the runnin of the flask api server
"""


from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import make_response
from flask import jsonify


app = Flask(__name__)

app.register_blueprint(app_views)


@app.errorhandler(404)
def errorHandle(error):
    """takes and handles 404 errors with custom message"""

    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
