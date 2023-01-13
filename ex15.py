from sys import argv
# in command lines , accept two parameters
script, fileName = argv
# open the file you give
txt = open(fileName)

print(f"Here's your file {fileName}")
# get the content of the file
print(txt.read())
txt.close()
print("Type the filename again:")
fileAgain = input("> ")
# open the file and read it again.
txtAgain = open(fileAgain)
print(txtAgain.read())
txtAgain.close()
