code = input("Enter a line of plain text: ")
distance = int(input("Enter the distance value: "))
plainText = ''

for i in range(len(code)):
	char = code[i]
	if (char.isupper()):
		plainText += chr(ord(char) - distance)
	else:
		plainText += chr(ord(char) - distance)
print(plainText)
