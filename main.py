import random

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

print("************** Welcome to A3AJAGBE RPS Game **************\n")

print("Game Information: \nRock wins against scissors.\nScissors win against paper.\nPaper wins against rock.\n")

print("Instruction: Type 0 for Rock, 1 for Paper and 2 for Scissors\n")

images = [rock, paper, scissors]

choice = int(input("What is your choice? \n"))

if choice > (len(images)-1):
  print("Invalid Input\n")
else:
  print(images[choice])


print("Computer's choice: ")
random_choice = random.randint(0,2)
print(images[random_choice])

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

  










