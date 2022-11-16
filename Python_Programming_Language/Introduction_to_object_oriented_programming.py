"""
OOP is a programming paradigm that relies on the concept of classes and object. It is used to structure programs
 into reusable blueprints(usually called classes), which are used to create individual instances of objects.

 Building blocks of OOp are(Classes; Objects; Attributes; Methods)

 Classes: Are user-defined types that contains attributes and methods. Individual objects are created from a class.
 An example of a class is Animal, in which attributes will be named, group etc. & methods can include fly(), walk(),
 etc

 Objects: Are instances of classes.Objects are created with specific data. For example in our class example,
 we can create an object of the Animal class with different attributes value. Eg: an object dog of the Animal
 instance can have its name value as snake and its group value as reptile.

 in python, we use class to create objects An object is made up of attributes and methods An Attribute represent
 data about the object. for example: the name, color, the speed, the height
       wind_mill (color = red, speed = 50mph, height = 5x10ft)

 Methods represent functionality or tasks that the object can do for example, adjust the speed or
 change the color dynamically.


 class Fruit:
     def __init__(self):
        self.name = "apple"
        self.color = "red"

    my_fruit = Fruit()

 We can create attribute by using the self parameter followed by the name of the attribute, and then assign it to a
 value of our choice. then we can call our fruit class and assign it to a variable

 class"""
#
class Animal:

    name = "Cow"
    group = "Mammal"

    def get_name_group(self):
        return self.name + ":" + self.group


# object
cow = Animal()
print(cow.name, cow.group, cow.get_name_group())
