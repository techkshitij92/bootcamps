#print the welcome message
print("Something Something")
height = input("Enter the heights of the students seperated by space:\n").split()
for i in range (0,len(height)):
	height[i] = int(height[i])
#the sum() adds and returns all the elements in the passed list
sum_height = sum(height)
number_of_students = len(height)
average_height =  sum_height/number_of_students
print(average_height)