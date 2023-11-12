#!/usr/bin/python3
"""BaseModel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Initialize a new instance of BaseModel """

        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    vformated = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, vformated)
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
#storage.new(self)

    def __str__(self):
        """ string representation of the BaseModel """

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__
        )

    def save(self):
        """ Update the current datetime """

        self.updated_at = datetime.now()
#storage.save()

    def to_dict(self):
        """ returns a dictionary representation of the BaseModel instance """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
