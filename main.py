"""
A rock, paper, scissors game application between the system and the user.
"""
from image import logo, rock, paper, scissors
import random

# Default Displays
print(logo)
print('Welcome, read the information below if you are not familiar with the game.')
print('Game Information: \nRock wins against scissors.\nScissors win against paper.\nPaper wins against rock.\n')
print('Instruction: Type 0 for Rock, 1 for Paper and 2 for Scissors\n')

# Add the hand gestures in a list
images = [rock, paper, scissors]

# User starts the game
choice = int(input("What hand gesture is your choice? \n"))

# Make sure the user input is valid
if choice > (len(images) - 1) or choice < 0:
    print("Invalid hand gesture, read the game instruction above.\n")
else:
    print(images[choice])

# Computer prompt
print("Computer's choice: ")
random_choice = random.randint(0, 2)
print(images[random_choice])

# Compare both choices to determine the winner
if choice == 0 and random_choice == 2:
    print("You win")
elif choice == 0 and random_choice == 0:
    print("It's a draw, Try Again")
elif choice == 2 and random_choice == 1:
    print("You win")
elif choice == 2 and random_choice == 2:
    print("It's a draw, Try Again")
elif choice == 1 and random_choice == 0:
    print("You win")
elif choice == 1 and random_choice == 1:
    print("It's a draw, Try Again")
else:
    print("You lose, Try Again!!!")
