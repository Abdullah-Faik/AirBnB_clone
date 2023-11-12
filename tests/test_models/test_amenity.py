import unittest
from models.amenity import Amenity
'''
    unit test class for models/amenity.py
'''


class testAmenity(unittest.TestCase):
    '''
        class testAmenity inherits from unittest.TestCase
        it has all the test case needed to test Amenity class
    '''

    def test_attributes(self):
        '''this function tests the attributes'''

        self.assertIsInstance(Amenity.name, str)


if __name__ == "__main__":
    unittest.main()
