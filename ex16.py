# readline
# Reads just one line of a txt
# 'w'  open for writing, truncating the file first

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# let the game starts
input("?")

print("Opening the file...")
# if the file is not existed we will build it.
target = open(filename, "w")

print("Truncating the file. Goodbye!")
# clear the whole file contents
target.truncate()

print("Now I'm going to ask u for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now I'm going to write these to the file.")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
target.close()
