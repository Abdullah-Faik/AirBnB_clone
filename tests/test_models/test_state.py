import unittest
from models.state import State
'''
    unit test class for models/state.py
'''


class testState(unittest.TestCase):
    '''
        class testState inherits from unittest.TestCase
        it has all the test case needed to test State class
    '''


    def test_attributes(self):
        '''this function tests the attributes'''

        self.assertIsInstance(State.name, str)

if __name__ == "__main__":
    unittest.main()
