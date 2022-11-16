"""
Attributes are information stored in class.
class attributes are attributes declared inside the class definition but outside of the methods.
"""


# class
class Animal:

    group = "Mammal"
    can_walk = True

    def __init__(self, name):
        self.name = name


cat = Animal("Cat")
dog = Animal("Dog")


print(cat.name)
print(dog.name)