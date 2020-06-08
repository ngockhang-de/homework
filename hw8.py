import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class EmailDescriptor:
    def __init__(self):
        self.email = None

    def __get__(self, instance, owner):
        return self.email

    def __set__(self, instance, value):
        if re.search(regex, value):
            self.email = value
        else:
            raise ValueError("Non valid email format")


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()


# my_class.email = "aalidemail@gmail.com"
# print(my_class.email)
# my_class.email = "novalidemail"
# print(my_class.email)


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


class NewClass:
    pass


c = MyClass()
b = MyClass()
e = NewClass()
assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:

    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return obj.value

    def __set__(self, obj, value):
        if isinstance(value, int):
            obj.value = value
        else:
            raise TypeError("Value should be integer")


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10
assert data_row.number != new_data_row.number
