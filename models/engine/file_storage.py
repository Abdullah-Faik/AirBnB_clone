#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User

'''
    this module serializes instances to a JSON file
    and deserializes JSON file to instances:
'''


class FileStorage:
    '''
        class FileStorage that serializes instances to a JSON file
        and deserializes JSON file to instances:
        Private class attributes:
            __file_path: string - path to the JSON file (ex: file.json)
            __objects: dictionary - empty but will store all objects
        Public instance methods:
            all(self): returns the dictionary __objects.
            new(self, obj): sets in __objects the obj with key
            <obj class name>.id
            save(self): serializes __objects to the JSON file
            (path: __file_path).
            reload(self): deserializes the JSON file to __objects.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id'''
        objectKey = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[objectKey] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)'''
        object_dict = {}
        for key, value in FileStorage.__objects.items():
            object_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as jsonFile:
            json.dump(object_dict, jsonFile)

    def reload(self):
        ''' deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)'''

        # dictionary containes all user defined classes in the project
        definedClasses = {'BaseModel': BaseModel, 'User': User}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as jsonFile:
                serialized_dict = json.load(jsonFile)
            for value in serialized_dict.values():
                className = value["__class__"]
                newObj = definedClasses[className](**value)
                self.new(newObj)
