tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line"
backslashCat = "I'm \\ a \\ cat"
fatCat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
myName = '''
It looks good.
'''
print("hello\n{}".format("world"))
print(myName)
print(tabbyCat)
print(persianCat)
print(backslashCat)
print(fatCat)

# delete the character in front of \b
print("aaaaaaa\bbb")
print("aaaa\fddddd")
# use \u plus number means unicode character
print("\uFF43\u0E9F")
print("\u93E1")
print("\U00000010")
print("\101\102\103")  # ABC
print("\xEF")
