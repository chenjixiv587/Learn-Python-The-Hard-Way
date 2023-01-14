
# this one is like your scripts with argv
def printTwo(*args):
    arg1, arg2 = args
    print(type(args))
    print(f"arg1:{arg1}, arg2:{arg2}")
 
# ok, that *args is actually pointless, we can just do this


def printTwoAgain(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument


def printOne(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments


def printNone():
    print("I got nothing.")


printTwo("hello", "world")
printOne("hello")
printTwoAgain("hello", "world")
printNone()
