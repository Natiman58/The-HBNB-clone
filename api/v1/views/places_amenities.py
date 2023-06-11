#!/usr/bin/python3
"""
    A module to handle RESTFul API action on the
    link between Place and Amenity objects
    Many-TO-Many relationship
"""
from models import storage
from flask import jsonify, abort
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
def list_aminities_of_a_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenities = place.amenities
    amenity_list = [amenity.to_dict() for amenity in amenities]
    return jsonify(amenity_list), 200

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity_of_a_place_by_id(place_id, amenity_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    # if the amenity is not linked to the place; raise 404
    if amenity not in place.amenities:
        abort(404)
    # else just remove it from the relationship; amenites
    place.amenities.remove(amenity)

    storage.save()
    return jsonify({}), 200

@app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'], strict_slashes=False)
def link_amenity_to_a_place(place_id, amenity_id):
    place = storage.get(Place, place_id)
    if not place:
        abort( 404)

    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    # if the amenity is linked to the place; return it
    if amenity in place.amenities:
        return jsonify(amenity.to_dict()), 200
    # else add it to the amenities relationship
    place.amenities.append(amenity)
    storage.save()

    return jsonify(amenity.to_dict()), 201
