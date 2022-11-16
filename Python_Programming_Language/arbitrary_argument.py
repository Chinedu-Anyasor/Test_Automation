"""If you don't know how may arguments will be passed to your fxn, you can add * to the name of your parameter to
accept the parameter as a type.
 """


def add(*args):
    print(args[0] + args[1])
    add(2, 3)


"""
With the arbitrary arg, you can accept as much argument in your fxn

Arbitrary Keyword Arg If you do not know how many arguments will be passed to your fxn, you can add ** to the name of 
your parameter to accept the parameter as a dictionary """


