plainText = input("Enter a line of plain text: ")
distance = int(input("Enter the distance value: "))
code = ""

for ch in range(len(plainText)):
	char = plainText[ch]
	if (char.isupper()):
		code += chr(ord(char) + distance)
	else:
		code += chr(ord(char) + distance)
print(code)
