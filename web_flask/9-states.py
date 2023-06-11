#!/usr/bin/python3
"""
    A module to display the states and the ids
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states_route():
    """
        display the states
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    
    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<string:id>', strict_slashes=False)
def state_id(id=None):
    """
        display the states
    """
    state = storage.all(State).get('State.{}'.format(id))
    return render_template('9-states.html', states=state)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)