import Logo
print(Logo.logo)

import os

# Clear the terminal (Linux, macOS, Windows)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize the dictionary to store bids
bidDictionary = {}

# Get the first bid
name = input("What is your name? ")
bid = int(input("How much do you want to bid? "))
bidDictionary[name] = bid

# Loop to collect more bids
while True:
    question = input("Does any other person want to bid, answer by giving 'yes' or 'no': ").strip().lower()
    if question == 'yes':
        clear_terminal()
        name = input("What is your name? ")
        bid = int(input("How much do you want to bid? "))
        bidDictionary[name] = bid
    elif question == 'no':
        break

# Determine the highest bid
maxBid = 0
topBidder = None

for name, score in bidDictionary.items():
    # Check if the current score is higher than the maximum score found so far
    if score > maxBid:
        # Update the maximum score and corresponding bidder name
        maxBid = score
        topBidder = name

clear_terminal()

print(f"The highest bid was placed by {topBidder} with a bid of {maxBid} !!")
