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
user_choice = int(input("What hand gesture is your choice? \n"))

# Make sure the user input is valid
if user_choice > (len(images) - 1) or user_choice < 0:
    print("Invalid hand gesture, read the game instruction above.\n")
else:
    print(images[user_choice])

    # Computer prompt
    print("Computer's choice: ")
    computer_choice = random.randint(0, 2)
    print(images[computer_choice])

    # Compare both choices to determine the winner
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == computer_choice:
        print("It's a draw, Try Again")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    else:
        print("You lose, Try Again!!!")
