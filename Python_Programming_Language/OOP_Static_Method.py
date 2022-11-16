"""
Static methods are methods that are bound to the class rather than the class object. The other type of method
 requires initializing the class before use, but the static method does not require the class to be initialized. It
 can be used directly from the class.

 Static method can be created in 2 ways:
 1. Using built-in staticmethod() fxn;
 2. Using the @staticmethod annotation
"""

class Calculator:

    def add(num1, num2):
        return num1 + num2


Calculator.add = staticmethod(Calculator.add)
print("1 + 1 =", Calculator.add(1, 1))

# ------OR------


class Calculator2:

    @staticmethod
    def multiply(num1, num2):
        return num1 + num2


print("2 * 2 =", Calculator2.multiply(2, 2))
