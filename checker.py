oldFile = open("output.txt").read()
oldFile = str(oldFile)
oldFile = oldFile.split()
readLines = oldFile.count("--&&--")
print readLines

