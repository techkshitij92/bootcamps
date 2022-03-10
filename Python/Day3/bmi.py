#display the welcome message
print("Welcome,Enter the height and weight to find BMI")
#take the height and weight input
height = float(input("Enter your Height\n"))
weight = float(input("Enter your Weight\n"))
#finding the bmi using the formula
bmi = (weight/height ** 2)
#check bmi and print accordingly
if bmi < 18.5:
	print(f"Your bmi is {bmi},you are underweight.".format(bmi))
elif bmi <25:
	print(f"Your bmi is {bmi},you are normal weight.".format(bmi))
elif bmi <30:
	print(f"Your bmi is {bmi},you are overweight.".format(bmi))
elif bmi <35:
	print(f"Your bmi is {bmi},you are obese".format(bmi))
else :
	print(f"Your bmi is {bmi},you are clinically obese.".format(bmi))