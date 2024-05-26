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

q1 = int(input("What do you want to choose ? Type 0 for rock, 1 for paper and 2 for scissor"))


options = [rock, paper, scissors]

print(options[q1])

print("Computer choose:")

choose = random.randint(0, 2)

print(options[choose])

if q1 == 0:
    if choose == 0:
        print("It's a draw!")
    elif choose == 1:
        print("Computer won!")
    else:
        print("You won!!")
elif q1 == 1:
    if choose == 0:
        print("You won!!")
    elif choose == 1:
        print("It's a draw!")
    else:
        print("Computer won!")
elif q1 == 2:
    if choose == 0:
        print("Computer won!")
    elif choose == 1:
        print("You won!!")
    else:
        print("It's a draw!")
else:
    print("Error, You typed something else.")
