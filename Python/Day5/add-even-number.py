print("Some Welcome message")
#first lets define a varible to store the sum of the numbers
s = 0
#there can be different ways to do this 
#lets run a loop initiating from 1 and going all the way to 100
for i in range (1,101):
	if (i%2==0): # even number condition
		s += i # same as s = s+i
print(s)
#another way to do this would be to change increment to 2
s = 0
for i in range (0,101,2):
	s = s+i
print(s)