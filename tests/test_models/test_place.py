import unittest
from models.place import Place
'''
    unit test class for models/place.py
'''


class testPlace(unittest.TestCase):
    '''
        class testPlace inherits from unittest.TestCase
        it has all the test case needed to test place class
    '''

    def test_attributes(self):
        '''this function tests the attributes'''

        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
