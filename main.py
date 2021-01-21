"""
A rock, paper, scissors game application between the system and the user.
"""
from image import logo, rock, paper, scissors

# Default Displays
print(logo)
print('Welcome, read the information below if you are not familiar with the game.')
print('Game Information: \nRock wins against scissors.\nScissors win against paper.\nPaper wins against rock.\n')
print('Instruction: Type 0 for Rock, 1 for Paper and 2 for Scissors\n')

# User starts the game
choice = int(input("What hand gesture is your choice? \n"))

# Add the hand gestures in a list
images = [rock, paper, scissors]

# Make sure the user input is valid
if choice > (len(images) - 1) or choice < 0:
    print("Invalid hand gesture, read the game instruction above.\n")
else:
    print(images[choice])

