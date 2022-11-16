"""
Abstract class are classes that contains abstract methods. Abstract methods are methods that are decleared(has
parameters) but not implemented. A class inheriting from an Abstract class must implement that abstract methods.

Python has the built-in ABC(Abstract Base Class) module to enable to create and use abstract classes.

To declare an abstract class in python, the class metaclass value must be should be set abc.ABCMeta or alternatively
the class should inherit from abc.ABC class.

Each abstract method in the class must be annotated with the annotation @ abc.abstractmethod.

If the abstract class inherits from abc.ABC class then the register annotation should be used in the child rather
than inheriting the class.

Interface is similar to Abstract classes in such a way that it allows the defining abstract methods but the
difference in interface is limited to method definition only and the method implementation is not enforced when it is
subclass.

The best time to write an abstract class or interface is when you need a parent class that needs to enforce a logic
in its child classes. """

import abc


class IWebElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def set_style(self):
        pass


class DivElement(IWebElement):

    def get_name(self):
        return "div"

    def set_style(self, style):
        print("Div style", style)


class SpanElement(IWebElement):

    def get_name(self):
        return "span"

    def set_style(self, style):
        print("Span Style:", style)


class ButtonElement(IWebElement):

    def get_name(self):
        return "button"

    def set_style(self, style):
        print("Button Style:", style)


div_element = DivElement()
print(div_element.get_name())
div_element.set_style("width: 100px; height: 100px")

span_element = SpanElement()
print(span_element.get_name())
span_element.set_style("border: 1px solid red;")

button_element = ButtonElement()
print(button_element.get_name())
button_element.set_style("font-size: 20px; font-weight: bold;")
