
class Vehicle:

    def drive_direction(self):
        print("Vehicle: Drive Forward")


class Plane(Vehicle):

    def drive_direction(self):
        print("Plane: Drive Upward")


class Submarine(Vehicle):

    def drive_direction(self):
        print("Submarine: Drive Downward")


vehicle = Vehicle()
vehicle.drive_direction()

plane = Plane()
plane.drive_direction()

sub_marine = Submarine()
sub_marine.drive_direction()