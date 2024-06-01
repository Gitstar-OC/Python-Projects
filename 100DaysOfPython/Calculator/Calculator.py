# import random
import os
import Logo

print(Logo.logo)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1  / n2

operations = {
    "+": add,
    "-": subtract,
    "/": devide,
    "*": multiply
}

num1 = float(input("What's the first number ? : "))
for keys in operations:
    print(keys)
operationSymbol = input("Pick an operation : ")
num2 = float(input("What's the second number ? : "))

calculationFunction = operations[operationSymbol]
answer = calculationFunction(num1, num2)

print(f"{num1} {operationSymbol} {num2} = {answer}")

operationSymbol = input("Pick an operation : ")
num3 = input("What is the next number ? : ")
calculationFunction = operations[operationSymbol]
answer = calculationFunction(answer, num3)


# while True:


