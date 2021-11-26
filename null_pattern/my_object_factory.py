from my_class import MyClass
from null_class import NullClass

class MyObjectFactory:
    @staticmethod
    def create_object(value):
        if value == 'my_class':
            return MyClass()
        else:
            return NullClass()