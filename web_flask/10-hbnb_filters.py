#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
        """Displays the main HBnB filters HTML page."""
            states = storage.all("State")
                amenities = storage.all("Amenity")
                    return render_template("10-hbnb_filters.html",
