
#take input from the user
year = int(input("Enter year :\n"))
#using nested if...else to check if it is a leap year.
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("The Year is a leap year.")
        else:
            print("The Year is not a leap year.")
    else:
        print("The Year is a leap year.") 
else:
    print("The Year is not a leap year.")