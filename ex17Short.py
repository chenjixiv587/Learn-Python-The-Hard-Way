from sys import argv
script, fromFile, toFile = argv
open(toFile, "w").write(open(fromFile).read())
