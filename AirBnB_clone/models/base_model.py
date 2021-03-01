#!/usr/bin/python3

'''
BaseModel: defines all common attributes/methods for other classes
'''

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    '''class BaseModel'''
    def __init__(self, **Kwargs):
        '''construtor of class'''
        if Kwargs is not None and Kwargs:
            for key, value in Kwargs.items():
                if key in ('created_at', 'updated_at'):
                    second = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, second)
                elif key != '__class__':
                    setattr(self, key, value)

        if "id" not in Kwargs.keys():
            self.id = str(uuid4())

        if "created_at" not in Kwargs.keys():
            self.created_at = datetime.today()

        if "updated_at" not in Kwargs.keys():
            self.updated_at = datetime.today()

        if Kwargs is None or len(Kwargs) == 0:
            storage.new(self)

    def __str__(self):
        '''overwrites the method __str__'''
        str_name = "[{:s}] ({}) {}"
        return str_name.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''update the updated_a attribute'''
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        '''return the dict of class'''
        dictionary = dict(self.__dict__)
        dictionary_update = {'created_at': self.created_at.isoformat(),
                             'updated_at': self.updated_at.isoformat()}
        dictionary.setdefault('__class__', self.__class__.__name__)
        dictionary.update(dictionary_update)
        return dictionary
