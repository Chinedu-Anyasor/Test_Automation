"""Using the OOP feature Inheritance, create a class Animal with the method sound() and then create a Cat and Dog
class that inherits from the Animal class. The Cat and Dog class should override the sound class and print a different
sound. """


class Animal:

    def sound(self):
        return "Unknown"


class Cat(Animal):

    def sound(self):
        return "Meow"


class Dog(Animal):

    def sound(self):
        return "Barking"


cat = Cat()
print(cat.sound())

dog = Dog()
print(dog.sound())
