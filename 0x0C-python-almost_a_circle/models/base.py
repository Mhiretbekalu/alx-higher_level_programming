#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        with public attribute id
        :param id:
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file"""
        for i in (list_objs):
            dic_1 = i.to_dictionary()

            name = i.__class__.__name__ + ".json"
            with open(name, "w") as f:
                f.write(cls.to_json_string(dic_1))

    @classmethod
    def save_to_file(cls, list_objs):
        '''method: save_to_file
        '''
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                tmp_dict = cls.to_dictionary(obj)
                list_dicts.append(tmp_dict)
            json_L_of_D = cls.to_json_string(list_dicts)
        else:
            json_L_of_D = "[]"

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            file.write(json_L_of_D)

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        output = []
        try:
            fname = cls.__name__ + ".json"
            with open(fname, "r") as f:
                ppd = cls.from_json_string(f.read())
                for i in ppd:
                    output.append(cls.create(**i))
            return output
        except:
            return output
