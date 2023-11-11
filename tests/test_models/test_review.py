import unittest
from models.review import Review
'''
    unit test class for models/review.py
'''


class testReview(unittest.TestCase):
    '''
        class testReview inherits from unittest.TestCase
        it has all the test case needed to test Review class
    '''


    def test_attributes(self):
        '''this function tests the attributes'''

        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

if __name__ == "__main__":
    unittest.main()
