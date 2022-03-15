#print some display message
print("Something Something")
scores = input("Enter the scores of the students seperated by space:\n").split()
for i in range (0,len(scores)):
	scores[i] = int(scores[i])
#max() returns the maximum values from a list
#there are different ways to find maximum values using loop also
max_score = max(scores)
print(max_score)