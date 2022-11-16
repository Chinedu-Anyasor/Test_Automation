"""
function is a set of instruction to perform a specific task.

Eg. Eat Cookies fxn.
Actions: Open mouth; insert cookies; chew; swallow.
Each of this actions is a task on its own and we still bundle them under the umbrella of eat cookies

1st- define a fxn with "def"
2nd- choose a name for the fxn
3rd- set of round brackets
4th- colon
5th- body(indented)
6th- variable a & b are the only variable inside the fxn.
if we try to access them from anywhere else, we will get an error.
They are local variables to our fxn but are strangers everywhere else.

def multiply
    a = 2
    b = 3
    :return a * b
multiply()

fxn also have outcome/output "axb" and we pass it into something called a return statement.
A return statement represents the end of the fxn.

That means any line of code we include below it will not be under the umbrella of multiply.

A valid return statement always includes some kind of data-integer, boolean, strings, list.

Just like human, we call fxn by its name "multiply".
Unlike human, we also add a set of round brackets to the end of the score.

We use parameter (to call multiple fxn) instead of variable. Parameters are used as placeholders. we get to decide
which value they represent only when it is time to call the fxn, not when to define it.
We use argument to assign values to our parameters. Parameters are basically placeholders for arguments.
"""

print("function\n")


def greet():
    print("Hello world from python")


def goodbye():
    print("Thank You")
    print("Good bye")


greet()
goodbye()

print("continuation\n")


def add(num1, num2):
    result = num1 + num2
    print(result)


def subtract(num1, num2):
    result = num1 - num2
    print(result)


def multiply(num1, num2, num3):
    result = num1 * num2 * num3
    print(result)


add(4, 3)
subtract(7, 2)
multiply(3, 4, 5)


def validate_username():
    pass