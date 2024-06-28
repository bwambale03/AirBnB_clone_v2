#!/usr/bin/python3
"""
This script starts a Flask web application with the following functionalities:
- The web application listens on 0.0.0.0, port 5000.
- It fetches data from the storage engine (FileStorage or DBStorage) via the `storage` object.
- It defines a route `/states_list` that displays a HTML page with a list of all State objects present in DBStorage, sorted by name.
- The HTML page includes:
    - An H1 tag with the text “States”.
    - A UL tag with the list of all State objects, each described by its ID and name inside an LI tag.
- The script ensures the current SQLAlchemy Session is removed after each request by declaring a method to handle `@app.teardown_appcontext` and calling `storage.close()` within this method.
- All route definitions use the `strict_slashes=False` option.
"""

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
