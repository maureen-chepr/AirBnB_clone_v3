#!/usr/bin/python3
"""Index section"""
from models import storage
from api.v1.views import app_views
from flask import jsonify
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


@app_views.route('/status')
def getStatus():
    """gets status"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def stats():
    """
        return dict count of data
    """
    my_dict = {"states": storage.count(State),
               "cities": storage.count(City),
               "places": storage.count(Place),
               "users": storage.count(User),
               "amenities": storage.count(Amenity),
               "reviews": storage.count(Review)}
    return jsonify(my_dict)
