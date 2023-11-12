#!/usr/bin/python3
from models.base_model import BaseModel
'''This module in the User class module'''


class User(BaseModel):
    '''class User inherits from BaseModel
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
