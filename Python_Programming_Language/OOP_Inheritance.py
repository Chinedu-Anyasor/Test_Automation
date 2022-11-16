"""
Inheritance is the capability of one class to derive or inherit the attributes and methods from another class.
The class that derives properties is called "Derived Class" or "Child class"
The class from which the properties are being derived is called the "base class" or "parent class"
"""


class Vehicle:

    model = "Unknown"
    make = "Unknown"
    production_year = "1990"

    def print_vehicle_info(self):
        print("\nVehicle {", self.make, ",", self.model + " }")


class Car(Vehicle):

    wheel_count = 4

    def __init__(self, make, model):
        self.model = model
        self.make = make


class Plane(Vehicle):

    model = "Aeroplane"
    make = "Boeing"


vehicle1 = Vehicle()
vehicle1.print_vehicle_info()

car1 = Car("Toyota", "Camry")
car1.print_vehicle_info()

plane1 = Plane()
plane1.print_vehicle_info()