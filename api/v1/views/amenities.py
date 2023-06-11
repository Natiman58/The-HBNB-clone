#!/usr/bin/python3
"""
    A module to handle RESTFul API actions for Amenity Obj:
    GET, POST, PUT, DELETE
"""
from flask import request, jsonify, abort
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity_by_amenity_id(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict()), 200

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity_by_amenity_id(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if  not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()

    return jsonify({}), 200

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    data = request.get_json()
    print(data)
    if not data:
        return jsonify({'Not a JSON'}), 400
    if 'name' not in data:
        return jsonify({'Missing name'}), 400

    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()

    return jsonify(amenity.to_dict()), 201

@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity_by_amenity_id(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({'Not a JSON'}), 400

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)

    storage.save()

    return jsonify(amenity.to_dict()), 200
