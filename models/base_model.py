#!/usr/bin/python3
"""
    A base model for all the objects
"""
from uuid import uuid4
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
        A base model for all the objects
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)


    def __init__(self, *args, **kwargs):
        from models import storage
        if kwargs:
            if 'id' not in kwargs:
                self.id = str(uuid4())
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            #storage.new(self) removed

    def __str__(self):
        """
            returns the string representation of the object
            class name + id + dict(attribures list)
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the updated at attribute with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)  # moved to here
        storage.save()

    def to_dict(self, include_password=False):
        """
            returns all the attributes in the class obj
            use password only when to store it in FS
        """
        d = self.__dict__.copy()
        if '_sa_instance_state' in d:
            del d['_sa_instance_state']
        d['__class__'] = self.__class__.__name__
        if self.created_at is not None:
            d['created_at'] = self.created_at.isoformat()
        if self.updated_at is not None:
            d['updated_at'] = self.updated_at.isoformat()
        if not include_password and 'password' in d:
            del d['password']
        return d

    def delete(self):
        """
            To delete the current instance from the storage(models.storage)
        """
        from models import storage
        storage.delete(self)