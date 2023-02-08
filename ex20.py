from sys import argv
script, inputFile = argv

# show all the contents of the file


def printAll(f):
    print(f.read())

# make the pointer to the beginner


def rewind(f):
    f.seek(0)

# every time show the one line of the file


def printALine(lineCount, f):
    print(lineCount, f.readline())


currentFile = open(inputFile)
print("First let's print the whole file:\n")
printAll(currentFile)
print("Now let's rewind, kind of like a tape")
rewind(currentFile)
print("Let's print three lines:")
currentLine = 1
printALine(currentLine, currentFile)
currentLine += 1
printALine(currentLine, currentFile)
currentLine += 1
printALine(currentLine, currentFile)
