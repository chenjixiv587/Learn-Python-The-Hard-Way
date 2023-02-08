from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print(f"Copying from {fromFile} to {toFile}")
# We could do these two on one line, how?
InFile = open(fromFile)
inData = InFile.read()

# inData = open(fromFile).read()
print(f"The input file is {len(inData)} bytes long")

print(f"Dose the output file exists? {exists(toFile)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input('?\t')

outFile = open(toFile, "w")
outFile.write(inData)

print("Alright, all done.")

outFile.close()
InFile.close()
