#!/usr/bin/python3

'''
FileStorage: instances to a JSON file and deserializes JSON file to instances
'''
import json


class FileStorage:
    '''class FileStorage'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.setdefault(key, obj)

    def save(self):
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict.setdefault(key, value.to_dict())

        with open(self.__file_path, 'w', encoding="utf-8") as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as my_file:
                from models.base_model import BaseModel
                obj = json.load(my_file)

            for key, value in obj.items():
                instance = eval(value.get('__class__') + "(**value)")
                FileStorage.__objects.setdefault(key, instance)
        except:
            pass
