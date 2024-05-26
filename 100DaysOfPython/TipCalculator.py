print("welcome to the calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("In how many people you want to split the bill in between?"))

tipAsPercent = tip / 100
totalTip = bill * tipAsPercent
totalBill = bill + totalTip
billPerPerson = totalBill / people 
finalAmount = round(billPerPerson, 2)

print(f"Each one should pay :${finalAmount}")