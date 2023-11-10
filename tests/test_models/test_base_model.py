import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid
'''
    unit test class for all the function exit in models/base_model.py
'''


class testBaseModel(unittest.TestCase):
    '''
        class testBaseModel inherits from unittest.TestCase
        it has all the test case needed to test BaseModel class
    '''

    def test_init(self):
        '''test  def __init__(self): function'''
        baseModel1 = BaseModel()
        self.assertIsInstance(baseModel1.id, str)
        self.assertIsInstance(baseModel1.created_at, datetime)
        self.assertIsInstance(baseModel1.updated_at, datetime)

        # tests of task4 (kwargs has a value)
        my_dict = {}
        my_dict["id"] = str(uuid.uuid4())
        my_dict["created_at"] = str(datetime.now().isoformat())
        my_dict["updated_at"] = str(datetime.now().isoformat())
        my_dict["my_number"] = 98
        my_dict["name"] = "my base model"

        baseModel2 = BaseModel(**my_dict)
        self.assertIsInstance(baseModel2.id, str)
        self.assertIsInstance(baseModel2.created_at, datetime)
        self.assertIsInstance(baseModel2.updated_at, datetime)
        self.assertEqual(baseModel2.__dict__["my_number"], 98)
        self.assertEqual(baseModel2.__dict__["name"], "my base model")

    def test_save(self):
        '''test def save(self): function'''
        baseModel1 = BaseModel()
        currentUpdated_at = baseModel1.updated_at
        baseModel1.save()
        self.assertNotEqual(currentUpdated_at, baseModel1.updated_at)

    def test_str(self):
        ''' test def __str__(self): function'''
        baseModel1 = BaseModel()
        resulted_Str = baseModel1.__str__()
        self.assertIsInstance(resulted_Str, str)
        self.assertIn("[BaseModel]", resulted_Str)
        self.assertIn(baseModel1.id, resulted_Str)
        self.assertIn("'created_at':", resulted_Str)
        self.assertIn("'updated_at':", resulted_Str)

    def test_to_dict(self):
        '''test def to_dict(self): function'''
        baseModel1 = BaseModel()
        resulted_dic = baseModel1.to_dict()
        self.assertIsInstance(resulted_dic, dict)
        self.assertIn("id", resulted_dic)
        self.assertIn("updated_at", resulted_dic)
        self.assertIn("created_at", resulted_dic)
        self.assertEqual(resulted_dic["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
