#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# lists, [], for loop, in range, if else elif,

password = ""
for i in range(1, nr_letters + 1):
    letterPass = random.randint(0, 51)
    password += letters[letterPass]

for j in range(1, nr_symbols + 1):
    symbolPass = random.randint(0, 8)
    password += symbols[symbolPass]

for k in range(1, nr_numbers + 1):
    numberPass = random.randint(0, 8)
    password += numbers[numberPass]
print(password)


Code = ""

for i in range(1, nr_letters + 1):
    Code += random.choice(letters)
for j in range(1, nr_symbols + 1):
    Code += random.choice(symbols)
for k in range(1, nr_numbers + 1 ):
    Code += random.choice(numbers)
print(Code)

# Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# Create a string
password
# Convert string to list of characters
char_list = list(password)

# Shuffle the list
random.shuffle(char_list)

# Convert shuffled list back to string
shuffled_string = ''.join(char_list)

print(f"Original string: {password}")
print(f"Shuffled string: {shuffled_string}")


code = list(Code)
random.shuffle(code)
shuffledString = "".join(code)

print(f"Orignal Code {Code}")
print(f"Shuffled Code{shuffledString}")
