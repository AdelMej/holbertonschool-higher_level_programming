"""
File that contains a custom class
"""
import pickle


class CustomObject:
    """Class custom object"""
    def __init__(self, name, age, is_student):
        """CustomObject constructor"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the custom object attributes"""
        print("Name: {:s}".format(self.name))
        print("Age: {:d}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """serializing method"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """deserialize a serialized pickle file"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
