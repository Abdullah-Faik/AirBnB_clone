import unittest
from models.user import User
'''
    unit test class for models/user.py
'''


class testUser(unittest.TestCase):
    '''
        class testUser inherits from unittest.TestCase
        it has all the test cases needed to test User class
    '''


    def test_attributes(self):
        '''This method tests User class attributes'''

        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)



if __name__ == "__main__":
    unittest.main()
