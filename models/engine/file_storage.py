#!/usr/bin/python3
import json
import os
'''
    this module serializes instances to a JSON file and deserializes JSON file to instances:
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
            new(self, obj): sets in __objects the obj with key <obj class name>.id
            save(self): serializes __objects to the JSON file (path: __file_path).
            reload(self): deserializes the JSON file to __objects.
    '''


    __file_path = "file.json"
    __objects = {}


    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id'''
        objectKey = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[objectKey] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path)'''
        obj = FileStorage.__objects
        #__objects: dictionary - empty but will store all objects by
        # <class name>.id (ex: to store a BaseModel object with id=12121212,
        # the key will be BaseModel.12121212)
        obj_dict = {o: obj[o].to_dict() for o in obj.keys()}
        with open(FileStorage.__file_path, "w") as jsonFile:
            json.dump(obj_dict, jsonFile)


    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def reload(self):
        ''' deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, 
        no exception should be raised)'''

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as jsonFile:
                obj_dict = json.load(jsonFile)
