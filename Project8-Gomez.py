firstTextFile = input("Name of first text file: ")
secondTextFile = input("Name of second text file: ")
firstFile = open(firstTextFile, 'r')
secondFile = open(secondTextFile, 'w')
for line in firstFile:
    secondFile.write(line)
firstFile.close()
secondFile.close()
