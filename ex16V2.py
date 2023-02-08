from sys import argv
script, filename = argv
target = open(filename, "r")
contents = target.read()
# let the point gose to the beginner
target.seek(0)
contentsList = target.readlines()
print(contentsList)
print(contents)
target.close()
