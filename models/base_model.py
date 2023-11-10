#!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import *
'''
    class BaseModel defines all common attributes/methods for other classes.

    Public instance attributes:
    - id: string - assign with an uuid when an instance is created.
    - created_at: datetime - assign with the current datetime when
        an instance is created.
    - updated_at: datetime - assign with the current datetime when
        an instance is created
    and it will be updated every time you change your object.
    - __str__: should print: [<class name>] (<self.id>) <self.__dict__>

    Public instance methods:
    - save(self): updates the public instance attribute updated_at with
        the current datetime.
    - to_dict(self): returns a dictionary containing all keys/values
        of __dict__ of the instance.
'''


class BaseModel:
    '''The BaseModel class declaration'''

    def __init__(self, *args, **kwargs):
        '''the constructor'''

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            regex_Str = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, regex_Str)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value

    def save(self):
        '''This function is called after any modification in the instance
        to change the value of updated_at attribute'''
        self.updated_at = datetime.now()
        


    def __str__(self):
        '''this function returns the string representation of
        the class instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        ''' returns a dictionary containing all keys/values of __dict__ of
        the instance:
        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name
        of the object
        created_at and updated_at must be converted to string object in
        ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        you can use isoformat() of datetime object'''

        instanceDict = {}

        for key, value in self.__dict__.items():
            if key == "created_at":
                instanceDict.update({"created_at":
                                     str(self.created_at.isoformat())})
            elif key == "updated_at":
                instanceDict.update({"updated_at":
                                     str(self.created_at.isoformat())})
            else:
                instanceDict.update({key: value})

        instanceDict.update({"__class__": self.__class__.__name__})

        return instanceDict
