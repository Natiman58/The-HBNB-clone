#!/usr/bin/python3
"""
    Displying from the db onto the filters section
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import uuid

app = Flask(__name__)

@app.route('/101-hbnb', strict_slashes=False)
def hbnb_filters():
    """
        displays the filters
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    places = sorted(storage.all(Place).values(), key=lambda place: place.name)
    #reviews = sorted(storage.all(Review).values(), key=lambda review: review.id)
    #print(reviews)
    #print(places)




    cities_by_state = {}

    for state in states:
        cities = sorted(state.cities, key=lambda city: city.name)
        cities_by_state[state.id] = cities

    review_by_place = {}
    for place in places:
        reviews = sorted(place.reviews, key=lambda review: review.place_id)
        review_by_place[place.id] = reviews
    print(review_by_place)
    return render_template('101-hbnb.html',
                           states=states,
                           cities=cities,
                           amenities=amenities,
                           cities_by_state=cities_by_state,
                           places=places,
                           cache_id=str(uuid.uuid4()),
                           reviews = review_by_place)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
