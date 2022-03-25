def primecheck(number):
	flag = 0
	for i in range (2,number):
		if (number%i==0):
			flag = 1
			break
	if (flag == 0):
		print("The number is prime.")
	else :
		print("The number is not prime.")
n = int(input("Enter the number to check for prime : \n"))
primecheck(number = n)