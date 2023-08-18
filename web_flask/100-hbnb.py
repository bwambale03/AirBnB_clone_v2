#!/usr/bin/python3
"""
starts a Flask web application. Listens on 0.0.0.0 at port 5000
Routes:* /hbnb: Display the HTML page for hbnb page
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@route('/hbnb', strict_slashes=False)
def hbnb():
    """this displays the HTML page for hbnb page"""
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    states = storage.all("State")

    return render_template("100-hbnb.html",
                           amenities = amenities,
                           places = places,
                           states = states)
@app.teardown_appcontent
def teardown(except=None):
    """this removes the SQLAlchemy sesssion"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
