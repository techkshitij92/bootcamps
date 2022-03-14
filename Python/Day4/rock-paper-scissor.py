#importing random
import random
#print the welcome message
print("Welcome to Rock-Paper-Scissor.")
print("Enter 0 for rock, 1 for paper, 2 for scissor.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
#ask for the input and store in choice
user_choice = int(input("What would you like to choose?\n"))
#randint() - used to generate random integer between given values
if user_choice >=0 and user_choice <=2:
	print(game[user_choice])
	computer_choice = random.randint(0,2)
	print("Computer chose : \n",game[computer_choice])
	if user_choice == 0 and computer_choice == 2:
		print("You win!")
	elif computer_choice == 0 and user_choice == 2:
		print("You lose")
	elif computer_choice > user_choice:
		print("You lose")
	elif user_choice > computer_choice:
		print("You win!")
	elif computer_choice == user_choice:
		print("It's a draw")
else :
	print("Wrong input!!!!!,Try Again ")