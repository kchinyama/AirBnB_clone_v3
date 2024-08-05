#!/usr/bin/python3
"""script to manage the runnin of the flask api server
"""


from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def closeApp():
    """closes the storage session of the database"""

    return storage.close()


if __name__ == "__main__":
    HOST=getenv('HBNB_API_HOST', '0.0.0.0')
    PORT=int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True)
