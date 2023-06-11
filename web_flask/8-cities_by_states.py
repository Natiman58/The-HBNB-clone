#!/usr/bin/python3
"""
    A module to display the cities in all the states
"""
from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
        lists all the cities
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    cities_by_state = {}

    for state in sorted_states:
        cities = sorted(state.cities, key=lambda city: city.name)
        cities_by_state[state.id] = cities

    return render_template('8-cities_by_states.html', states=sorted_states, cities_by_state=cities_by_state)

@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
