#print the welcome message
print("Welcome to the Love Calculator!")
#take the name inputs
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
#forming a combined string and turning it into lower case using lower()
lower_combined_string = (name1+name2).lower()
#counting the number of occurrences using count()
t=lower_combined_string.count("t")
r=lower_combined_string.count("r")
u=lower_combined_string.count("u")
e=lower_combined_string.count("e")

true = t + r + u + e

l=lower_combined_string.count("l")
o=lower_combined_string.count("o")
v=lower_combined_string.count("v")
e=lower_combined_string.count("e")
#note 'e' has been used two times in lines 12 and 19
love=l + o + v + e

score = true + love
print(score)

if (score < 10) or (score > 90):
	print(f"Your love score is {0}, you go together like coke and mentos.".format(score))
elif (score>=40) and (score<=50):
	print(f"Your score is {0}, you are alright together.".format(score))
else :
	print(f"Your score is {0}".format(score)) 