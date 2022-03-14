#This is still a Work in Progress,so wait a little
row1=["1","2","3"]
row2=["4","5","6"]
row3=["7","8","9"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
pos = input("Where do you want to put the treasure:\n")
answer = input("Enter your choice for the treasure:\n")
if pos[0]==answer[0] and pos[1]==answer[1]:
	print("You hit it right through\n")
	map[int(pos(0))-1][int(pos(1))-1]="T"
	print(f"{row1}\n{row2}\n{row3}")
else :
	print("Oops!!Bad Luck,Try Again")