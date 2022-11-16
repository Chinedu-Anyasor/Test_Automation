"""
Data Abstraction in python can be achieved through creating abstract classes or private attributes.

Data abstract hides the unnecessary code details from the user. When we don't want to give out or show sensitive data
from our class, data abstract is used to hide the data. """


class LoginSession:
    __email = "user@test.com"
    __password = "password"

    def get_email(self):
        return self.__email

    def get_password(self):
        return "********"


session = LoginSession()
print(session.get_email())
print(session.get_password())

"""
To create an object from a class, is called instantiation.
How to instantiate
<object name> = <class name>()
"""