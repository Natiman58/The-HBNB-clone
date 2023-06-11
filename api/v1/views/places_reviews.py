#!/usr/bin/python3
"""
    A module to handle RESTFul API requests for the
    Review object; PUT DELETE POST GET
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.review import Review
from models.place import Place
from models.user import User
from models import storage


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews_by_place_id(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews), 200

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_reviews_by_review_id(review_id):
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict()), 200

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_reviews_by_review_id(review_id):
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(Review)
    storage.save()

    return jsonify({}), 200

@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def create_reviews_by_place_id(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({'Not a JSON'}), 400
    if 'user_id' not in data:
        return jsonify({'Missing user_id'}), 400
    if 'text' not in data:
        return jsonify({'Missing text'}), 400

    user_id = data['user_id']
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    data['user_id'] = user_id
    data['place_id'] = place_id

    review = Review(**data)
    storage.new(review)
    storage.save()

    return jsonify(review.to_dict()), 201

@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review_by_review_id(review_id):
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({'Not a JSON'}), 400
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    storage.save()

    return jsonify(review.to_dict()), 200
