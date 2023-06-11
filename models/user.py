#!/usr/bin/python3
"""
    A module for a user
"""
from models.base_model import BaseModel, Base
from datetime import datetime
import json
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """
        A user class to represent a user
    """
    __tablename__ = 'users'
    __table_args__ = ({'mysql_default_charset': 'latin1'})
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False, default="")
    last_name = Column(String(128), nullable=False, default="")
    places = relationship("Place", cascade="all, delete", backref="user")
    reviews = relationship("Review", cascade="all, delete", backref="user")

    def __init__(self, password='', **kwargs):
        super().__init__(**kwargs)
        self.password = hashlib.md5(password.encode()).hexdigest()

    def update_password(self, new_password):
        self.password = hashlib.md5(new_password.encode()).hexdigest()

    def all(self):
        """
            lists all the users only
        """
        from models import storage

        all_objs = storage.all()
        obj_list = []
        for key, value in all_objs.items():
            class_name = key.split('.')[0]
            if class_name == "User":
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
            if class_name == "User":
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
            obj = storage.all()['User' + '.' + id]
            print(obj)

    def destroy(self, id):
        """
            TO destroy a user object based on the given id
        """
        from models import storage
        id_list = []
        all_objs = storage.all()
        for key in all_objs.keys():
            obj_id = key.split('.')[1]
            id_list.append(obj_id)
        if id in id_list:
            del storage.all()['User' + '.' + id]
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
            obj = storage.all()['User' + '.' + id]
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
            obj = storage.all()['User' + '.' + id]
            # replace the single quotes by double quotes
            json_string = full_dict.replace("'", "\"")
            # convert the dict string into valid json data
            json_data = json.loads(json_string)
            for key, value in json_data.items():
                setattr(obj, key, value)
            obj.save()
