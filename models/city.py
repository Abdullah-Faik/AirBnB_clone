#!/usr/bin/python3
from models.base_model import BaseModel
'''This module in the City class module'''


class City(BaseModel):
    '''
    class City inherits from BaseModel
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    '''

    state_id = ""
    name = ""
