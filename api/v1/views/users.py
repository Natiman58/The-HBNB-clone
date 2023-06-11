#!/usr/bin/python3
"""
    A module for handeling RESTFul API actions for User object
    GET, POST, PUT, DELETE
"""

from flask import request, jsonify, abort
from api.v1.views import app_views
from models import storage
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_by_id(user_id):
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict()), 200

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user_by_user_id(user_id):
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()

    return jsonify({}), 200

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'Not a JSON'}), 400
    if 'email' not in data:
        return jsonify({'Missing email'}), 400
    if 'password' not in data:
        return jsonify({'Missing password'}), 400

    user = User(**data)
    storage.new(user)
    storage.save()

    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user_by_user_id(user_id):
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({'Not a JSON'}), 400

    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'email']:
            setattr(user, key, value)
    storage.save()

    return jsonify(user.to_dict()), 200
