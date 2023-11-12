import unittest
from models.city import City
'''
    unit test class for models/city.py
'''


class testCity(unittest.TestCase):
    '''
        class testCity inherits from unittest.TestCase
        it has all the test case needed to test City class
    '''

    def test_attributes(self):
        '''this function tests the attributes'''

        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)


if __name__ == "__main__":
    unittest.main()
