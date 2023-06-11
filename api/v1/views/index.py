#!/usr/bin/python3
"""
    package that contains the necessary routes and logic for API endpoints.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User
from models.state import State


@app_views.route('/status', methods=['GET'])
def get_status():
    """
        api endpoint /status to get the status of api
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """
        an end point that retrieves the number of each objects by type
    """
    stats = {}
    obj_count = 0
    classes = [Amenity, Place, Review, User, City, State]

    for clss in classes:
        clss_name = clss.__name__
        obj_count = storage.count(clss)
        stats[clss_name.lower()] = obj_count
    return jsonify(stats)
