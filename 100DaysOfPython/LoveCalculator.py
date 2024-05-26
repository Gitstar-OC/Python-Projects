name1 = input("what is your name?")
name2 = input("what is your partner's or crush's name?")

combinedName = name1 + name2
lowerNames = combinedName.lower()

t = lowerNames.count("t")
r = lowerNames.count("r")
u = lowerNames.count("u")
e = lowerNames.count("e")

firstLetter = t + r + u + e

l = lowerNames.count("l")
o = lowerNames.count("o")
v = lowerNames.count("v")
e = lowerNames.count("e")
secondLetter = l + o + v + e

score = int(str(firstLetter) + str(secondLetter))


if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score < 50 and score > 40:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")