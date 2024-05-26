import random

coinToss = random.randint(0, 1)

if coinToss == 1:
    print("Heads")
else:
    print("Tails")

number = random.random
# This will print random float from 0 to 1, (1 not included) [0,1)