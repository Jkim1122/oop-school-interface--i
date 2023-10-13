from abc import ABC, abstractclassmethod

class Person(ABC):
    def __init__(self, name, age, role, password):
        self.name = name
        self.age = age     
        self.role = role
        self.password = password

    @abstractclassmethod
    def all_members(cls):
        pass