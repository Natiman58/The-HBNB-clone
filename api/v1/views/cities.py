#!/usr/bin/python3
"""
    A module for creating RESTful API for City objects
"""
from flask import jsonify, request, abort
from models.city import City
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_city_by_state_id(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities), 200

@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city_by_city_id(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict()), 200

@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city_by_city_id(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()

    return jsonify({}), 200

@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def create_city_by_state_id(state_id):
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({'Not a JSON'}), 400
    if 'name' not in data:
        return jsonify({'Missing name'}), 400
    data['state_id'] = state_id
    city = City(**data)

    storage.new(city)
    storage.save()

    return jsonify(city.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city_by_city_id(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({'Not a JSON'}), 400
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 200
