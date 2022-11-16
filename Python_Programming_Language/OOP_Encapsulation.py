
"""Encapsulation is the idea of enclosing information in a class and exposing only selected information. This puts
restrictions on accessing attributes and methods directly and can prevent the accidental modification of data. """

class User:
    __first_name = "Testify"
    __last_name = "QA"
    __attendance = 1

    def get_name(self):
        return "User-" + self.__first_name

    def get_attendance(self):  # This method has hidden the attendance value which is one but exposes attendance * 20
        value = self.__attendance * 20
        return value


user = User()
print(user.get_name())
print(user.get_attendance())