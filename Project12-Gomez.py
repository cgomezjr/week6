fileName = input("Enter file name: ")
f = open(fileName,'r')
data = f.read()


#data = [["Gomez",20,40],
#        ["Cardoza",25,40],
#        ["Baxter",30,40]]


print("%-15s %-15s %s" % ("Last Name","Hourly Wage","Hours Worked"))


for item in data:
  print(item[0]," "*(14-len(item[0])),
        item[1]," "*(14-len(str(item[1]))),
        item[2])

  
f.close()
