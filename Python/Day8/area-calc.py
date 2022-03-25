import math
h = int(input("Enter Height : "))
b = int(input("Enter Breadth : "))
cover = 5
def areacalc(height,breadth,cover):
	number_of_cans = math.ceil((height*breadth)/cover)
	print(f"Number of cans required ot paint : {number_of_cans}")
areacalc(height = h,breadth = b,cover = cover)