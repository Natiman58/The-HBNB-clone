#!/usr/bin/python3
"""
    module for a new view for State obj that handles
    all the default RESTFul API actions; GET, PUT, POST, DELETE
"""
from models import storage
from api.v1.views import app_views
from flask import jsonify
from models.state import State
from flask import abort, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states]), 200

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_by_id(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict()), 200

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state_by_id(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()

    return jsonify({}), 200

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    state = State(name=data['name'])

    storage.new(state)
    storage.save()

    return jsonify(state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    state = storage.get(State, state_id)
    if not state:
        return jsonify({'error': 'Not found'}), 400
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Not a JSON'}), 400
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    storage.save()

    return jsonify(state.to_dict()), 200
