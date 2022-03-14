import random
names_str = input("Enter everyone's names seperated by single space\n")
names = names_str.split()
print("The person who is going to pay is:\n",names[random.randint(0,len(names)-1)]) 