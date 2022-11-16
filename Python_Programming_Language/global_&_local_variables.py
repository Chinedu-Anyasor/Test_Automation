"""
Local variables are variables defined within/onside the scope of a fxn.
Global variables are variables defined outside the scope of a fxn.
Local are defined inside the fxn block and cannot be accessed outside that fxn
Global are accessible by all fxn as they are defined outside the fxn scope
"""

name = "Testify"  # Global variable


def hello():
    language = "python"  # local variable
    print(language)


"""Variable shadowing is the masking of the outer variable by the inner variable. This occurs when a variable in an 
inner scope has the same name as another variable defined in the outer scope """

name = "Testify"


def hello():
    name = "python"
    print(name)


"""
In the snippet above, the global variable name is shadowed by the local variable name in the hello fxn; if the 
hello fxn is invoked, python will be printed in the console """
