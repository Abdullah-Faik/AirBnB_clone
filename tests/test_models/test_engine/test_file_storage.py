import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
'''
    unit test class for all the function exit in
    models/engine/file_storage.py
'''


class testFileStorage(unittest.TestCase):
    '''
        class testFileStorage inherits from unittest.TestCase
        it has all the test case needed to test FileStorage class
    '''

    def setUp(self):
        '''This function runs only one time before any tests'''
        self.storage = FileStorage()

    def test_all(self):
        '''this function test all(self)'''
        objs = self.storage.all()
        self.assertIsInstance(objs, dict)
        self.assertNotEqual(objs, None)

    def test_new(self):
        '''this function tests new(self, obj)'''
        obj = BaseModel()
        self.storage.new(obj)
        allObjs = self.storage.all()
        self.assertNotEqual(len(allObjs), 0)
        self.assertIn(f'{obj.__class__.__name__}.{obj.id}', allObjs.keys())

    def test_save(self):
        '''this function tests save(self)'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", 'r') as json_file:
            data = json.load(json_file)
        self.assertIn(f'{obj1.__class__.__name__}.{obj1.id}', data)
        self.assertIn(f'{obj2.__class__.__name__}.{obj2.id}', data)

    def test_reload(self):
        '''this function tests reload(self)'''
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        self.storage.__objects = {}
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertNotEqual(len(all_objects), 0)
        self.assertIn(f'{obj1.__class__.__name__}.{obj1.id}', all_objects)
        self.assertIn(f'{obj2.__class__.__name__}.{obj2.id}', all_objects)

    def test_1__file_path(self):
        '''this function tests _file_path(self)'''
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_0__objects(self):
        '''this function tests _objects(self)'''
        pass


if __name__ == "__main__":
    unittest.main()
