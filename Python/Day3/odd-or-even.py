#Display the welcome message
print("Welcome to the program to check a number for odd or even")
#take user input and store it in a variable a
a=int(input("Enter Number to check :\n"))
#Using if...else to check and display the output
# '%' operator gives the remainder
if (a%2==1):
	print("The number is odd")
#if 'if' results in false the else block is executed
else :
	print("The number is even")