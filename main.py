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

choice = int(input("What is your choice? \n"))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

  print("Computer's choice: ")
  random_choice = random.randint(0,2)

  if random_choice == 0:
    print(rock)
  elif random_choice == 1:
    print(paper)
  else: 
    print(scissors)

  if choice == 0 and random_choice == 2:
    print("You won")
  elif choice == 2 and random_choice == 1:
    print("You won")
  elif choice == 1 and random_choice == 0:
    print("You won")
  else:
    print("You lost, Try Again!!!")

else: 
  print("Wrong input!!!")



