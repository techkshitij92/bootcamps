text = input("Enter the text to encrypt with ceaser cipher :\n")
n = int(input("Enter the shift number (Remember the number should be in between 0 and 25): \n"))
def cipher(text , n):
	result = ""
	for i in range(0,len(text)):
		char = text[i]
		if (char.isupper()): #.isupper returns true is the character in in upper case
			result += chr((ord(char) + n-65) % 26 + 65)
		else :
			result += chr((ord(char) + n-97) % 26 + 97)
	print(result)
cipher(text = text , n = n)