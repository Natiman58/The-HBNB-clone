#!/usr/bin/python3
"""
    A module for serialization and deserialization
"""
import json
import os
from datetime import datetime
from models.user import User
from models.base_model import BaseModel

from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review  import Review
import hashlib

class FileStorage:
    """
        stores the json files and the dict objects
    """
    __file_path = 'file.json'
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }
    
    def all(self, cls=None):
        """
            returns all the objects
        """
        if cls:
            obj_dict = {}
            for key, value in self.__objects.items():
                class_name = key.split('.')[0]
                input_cls_name = str(cls).split('.')[2].strip()[:-2]
                if(input_cls_name == class_name):
                    obj_dict[key] = value
            return obj_dict

        # if cls is none
        else:
            return self.__objects
    
    def new(self, obj):
        """
            saves the new obj in the __obj dict with key
            obj_class_name.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj
    
    def save(self):
        """ 
            saves the object into a json file;
            serialization
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, BaseModel):
                new_val = obj.to_dict()
                obj_dict[key] = new_val
            if isinstance(obj, datetime):
                new_val = datetime.isostream()
                obj_dict[key] = new_val
            if isinstance(obj, User):
                hashed_pwd = hashlib.md5(obj.password.encode()).hexdigest()
                obj.password = hashed_pwd
            else:
                obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f, indent=4)

    def reload(self):
        """
            deserializes the json file into a dict obj
        """
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, 'r') as f:
                    data = json.load(f)
                    for key, value in data.items():
                        class_name = key.split('.')[0]
                        obj_class = self.classes.get(class_name)
                        if obj_class:
                            obj = obj_class(**value)
                            self.__objects[key] = obj
            else:
                pass
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
            updates FS_storage to delete objs from __objects
            using the given class name and id
        """
        if obj is None:
            return
        key = obj.__class__.__name__ + '.' +  obj.id
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """
            to desrialize json file into objects
        """
        self.reload()

    def get(self, cls, id):
        """
            cls: class name
            id: string representing the id of the object
            returns the object based on the class and it's id
        """
        objects = self.all(cls)
        for key in objects.keys():
            obj_id = key.split('.')[1]
            if obj_id == id:
                return objects[key]
        return None

    def count(self, cls=None):
        """
            cls: class name
            returns: number of objects in the given class
        """
        if cls:
            return len(self.all(cls))
        else:
            objects_count = 0
            for clss in self.classes.values():
                objects_count += len(self.all(clss))
            return objects_count
