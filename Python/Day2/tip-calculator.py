#print the welcome message
print("Welcome to the tip calculator.")
#Ask for the total bill
#Forgot to add float in the first try! 
bill = float(input("What was the total bill?\n$"))
#Ask for the tip percentage
tip = int(input("How much tip would you like to give?10, 12 or 15\n"))
#Ask for the number of persons to split the bill between
persons = int(input("How many people to split the bill?\n"))
split = (bill+(tip*bill)/100)/7
#(round(split,2)) - rounds of the calculation to 2 decimal places
print("Each person should pay\n${}".format(round(split,2)))
