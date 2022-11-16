
def accept(cb):
    cb("Hello")


hello = lambda : print("me and you")
hello()
accept(lambda q: print(q))