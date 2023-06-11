#!/usr/bin/python3
"""
    A module for that Sate class
"""
from models.base_model import BaseModel, Base
from datetime import datetime
import json
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import environ
from models.city import City

class State(BaseModel, Base):
    """
        A class that represents a state obj
    """
    __tablename__='states'
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        # the reference from City object to State object is named "state"
        cities = relationship("City", cascade="all, delete", backref="state")

    elif environ.get('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            """
                Getter attribute cities
            """
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    def all(self):
        """
            lists all the states only
        """
        from models import storage

        all_objs = storage.all()
        obj_list = []
        for key, value in all_objs.items():
            class_name = key.split('.')[0]
            if class_name == "State":
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
            count the number of states
        """
        from models import storage

        all_objs = storage.all()
        obj_list = []
        for key, value in all_objs.items():
            class_name = key.split('.')[0]
            if class_name == "State":
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
            #class_name = all_objs[key].__class__.__name__
            obj = storage.all()['State' + '.' + id]
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
            del storage.all()['State' + '.' + id]
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
            obj = storage.all()['State' + '.' + id]
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
            obj = storage.all()['State' + '.' + id]
            # replace the single quotes by double quotes
            json_string = full_dict.replace("'", "\"")
            # convert the dict string into valid json data
            json_data = json.loads(json_string)
            for key, value in json_data.items():
                setattr(obj, key, value)
            print(obj)
            obj.save()
