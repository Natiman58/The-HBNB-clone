#!/usr/bin/python3
"""
    A module for the place class
"""
from models.base_model import BaseModel, Base
from datetime import datetime
import json
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

# create many-to-many relationship table b/n Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False),
                      mysql_default_charset="latin1"
                      )


class Place(BaseModel, Base):
    """
        A class representing a place object
    """
    __tablename__ = 'places'
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    city_id = Column(String(60), ForeignKey('cities.id') ,nullable=False)
    user_id = Column(String(60), ForeignKey('users.id') ,nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []


    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    else:
        @property
        def reviews(self):
            """
                a getter attribute
            """
            from models import storage
            place_list = []
            for place in storage.all(Place).values():
                if place.place_id == self.id:
                    place_list.append(place)
            return place_list

        @property
        def amenities(self):
            """
                getter attribute
            """
            from models import storage
            from models.amenity import Amenity
            amenity_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get(Amenity, amenity_id)
                if amenity:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            """
                Setter attribute amenities for FS
                adds an amenity id to the amenity_ids list
            """
            from models.amenity import Amenity
            if isinstance(amenity, Amenity):
                if amenity.id not in self.amenity_ids:
                    self.amenity_ids.append(amenity.id)

    def all(self):
        """
            lists all the Places only
        """
        from models import storage

        all_objs = storage.all()
        obj_list = []
        for key, value in all_objs.items():
            class_name = key.split('.')[0]
            if class_name == "Place":
                dict_value = value.to_dict()
                dict_value.pop('__class__', None)
                for key, value in dict_value.items():
                    if key in ['created_at', 'updated_at']:
                        dict_value[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                obj_str = f"[{class_name}] ({dict_value.get('id')}) {dict_value}"
                obj_list.append(obj_str)
        print(obj_list)

    def count(self):
        """
            count the number of users
        """
        from models import storage

        all_objs = storage.all()
        obj_list = []
        for key, value in all_objs.items():
            class_name = key.split('.')[0]
            if class_name == "Place":
                dict_value = value.to_dict()
                dict_value.pop('__class__', None)
                for key, value in dict_value.items():
                    if key in ['created_at', 'updated_at']:
                        dict_value[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                obj_str = f"[{class_name}] ({dict_value.get('id')}) {dict_value}"
                obj_list.append(obj_str)
        print(len(obj_list))

    def show(self, id):
        """
            shows the instance using the given id
        """
        from models import storage

        id_list = []
        all_objs = storage.all()
        for key in all_objs.keys():
            obj_id = key.split('.')[1]
            id_list.append(obj_id)
        if id in id_list:
            obj = storage.all()['Place' + '.' + id]
            print(obj)

    def destroy(self, id):
        """
            Destroys the instance using the given id
        """
        from models import storage
        id_list = []
        all_objs = storage.all()
        for key in all_objs.keys():
            obj_id = key.split('.')[1]
            id_list.append(obj_id)
        if id in id_list:
            del storage.all()['Place' + '.' + id]
            storage.save()

    def update(self, id, attr, value):
        """
            updates an instance to the given attribute and value
            for the given id
        """
        from models import storage
        id_list = []
        all_objs = storage.all()
        for key in all_objs.keys():
            obj_id = key.split('.')[1]
            id_list.append(obj_id)
        if id in id_list:
            obj = storage.all()['Place' + '.' + id]
            if '"' in value:
                claen_val = value.strip()[1:-1]  # remove the quotes
            else:
                claen_val = value
            setattr(obj, attr, claen_val)
            obj.save()

    def update_dict(self, id, full_dict):
        """
            updates an instance using the given id and dict
        """
        from models import storage
        id_list = []
        all_objs = storage.all()
        for key in all_objs.keys():
            obj_id = key.split('.')[1]
            id_list.append(obj_id)
        if id in id_list:
            obj = storage.all()['Place' + '.' + id]
            # replace the single quotes by double quotes
            json_string = full_dict.replace("'", "\"")
            # convert the dict string into valid json data
            json_data = json.loads(json_string)
            for key, value in json_data.items():
                setattr(obj, key, value)
            obj.save()
