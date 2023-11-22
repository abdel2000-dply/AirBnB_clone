#!/usr/bin/python3

import uuid
import datetime
class BaseModel:
    '''This is the root model that defines all the common atributes/methods
    '''
    def __init__(self, *args, **kwargs):
        '''This initializes the public attributes'''
        if kwargs is not None and kwargs != {}:
            for keys in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())#creates a universal unique id every time an object is instantiated
            self.created_at = datetime.datetime.now()#gives us the real time wn object is created
            self.updated_at = datetime.datetime.now()#gives the reattime an object is updated

    def __str__(self):
         '''thsl returns the official string representation of an object '''
         return f" {base.__class__.__name__} {self.id} {self.__dict__}"

    def save(save):
        '''updates the public instance attribute'''
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__instance
        '''
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        
base = BaseModel()
print(base .id)
print(base.created_at)
print(base.updated_at)
print(base)
