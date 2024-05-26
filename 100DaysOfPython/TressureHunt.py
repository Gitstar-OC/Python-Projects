print("Welcome to Treasure Island, your mission is to find the treasure.")

q1 = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\". ").lower()

if q1 == "left":
    q2 = input('You are near a river, What would you like to do? Type "swim" or "wait".').lower()
    if q2 == "wait":
        q3 = input('Now there are three doors in front of you, which one will you choose? Type "Red", "Yellow" or "Blue".').lower()
        if q3 == "yellow":
            print("Congratulations, you win the treasure!")
        elif q3 == "red":
            print("You got burned by fire, Game Over!")
        elif q3 == "blue":
            print("You got eaten by beasts, Game Over!")
        else:
            print("Game Over")
    elif q2 == "swim":
        print("You got attacked by trout, Game Over!")
    else:
        print("Game Over!")
elif q1 == "right":
    print("You fall into a hole, Game Over!")
else:
    print("Game Over")
