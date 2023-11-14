#!/usr/bin/python3
"""Defines the base module."""


import json
import ast
import sys
import csv
"""Defines the imported modules."""


class Base:
    """Defines the class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Defines a class constuctor for the Base class."""

        if id is not None and isinstance(id, int) == True:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """Defines a static method. Returns list_dictionaries as a JSON str."""

        if list_dictionaries == None or list_dictionaries == []:
            empty = "[]"
            return empty
        elif type(list_dictionaries) == list:
            return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """Defines the class method that writes list_objs to a JSON string."""

        if list_objs == None:
            list_objs = []
        if isinstance(list_objs, list):
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            filename = cls.__name__ + ".json"
            json_string = cls.to_json_string(list_dicts)
            with open(filename, "w") as json_file:
                json.dump(json_string, json_file)


    @staticmethod
    def from_json_string(json_string):
        """Defines a static method that returns json_string as a list."""

        if json_string == None or json_string == "":
            empty = []
            return empty
        if type(json_string) == str:
            list_of_dicts = ast.literal_eval(json_string)
            return list_of_dicts


    @classmethod
    def create(cls, **dictionary):
        """Defines a class method. Returns a set instance of a class object."""

        from models.rectangle import Rectangle
        from models.square import Square
        """Defines the imported modules methods Rectangle and Square."""

        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy


    @classmethod
    def load_from_file(cls):
        """Defines a class method. Returns a list of instances."""

        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r") as my_file:
                json_string = json.load(my_file)
            data = Base.from_json_string(json_string)
            instances = [cls.create(**d) for d in data]
        except FileNotFoundError:
            return []
        return instances


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Defines the class method that serializes in CSV."""

        if list_objs == None or len(list_objs) == 0:
            return []
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            list_dicts = [obj.to_dictionary for obj in list_objs]
            writer.writerow(list_dicts)


    @classmethod
    def load_from_file_csv(cls):
        """Defines a class method that deserializes in CSV."""

        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", newline="") as csv_file:
                reader = csv.reader(csv_file)
                instance = [cls.create(**row) for row in reader]
            return instances
        except FileNotFoundError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """Defines a static method that draws all Rectangles and Squares."""

    pass
