#!/usr/bin/python3
"""Base class"""


class Base():
    """first class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation"""
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string"""
        my_list = []
        fname = cls.__name__ + ".json"
        if (list_objs is not None):
            for indx in list_objs:
                my_list.append(indx.to_dictionary())
        jstr = cls.to_json_string(my_list)
        with open(fname, "w") as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string"""
        if (json_string is None or len(json_string) == 0):
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set """
        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        elif (cls.__name__ == "Square"):
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        my_list = []
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r") as jsonfile:
                listJson = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in listJson]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list objects in csv format and save"""
        if list_objs is None or list_objs == []:
            my_list = "[]"
        else:
            my_list = cls.to_json_string(
                [o.to_dictionary() for o in list_objs])
        new_file = cls.__name__ + ".csv"
        with open(new_file, "w") as f:
            f.write(my_list)

    @classmethod
    def load_from_file_csv(cls):
        """ deserializes csv of the list of instances """
        fname = cls.__name__ + ".csv"
        if not os.path.exists(fname):
            return []
        list_dict = []
        with open(fname, "r") as f:
            str1 = f.read()
            list_dict = cls.from_json_string(str1)
        return [cls.create(**d) for d in list_dict]
