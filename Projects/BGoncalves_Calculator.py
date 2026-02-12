# Name: Broderick Goncalves
# Date: 2 / 15 / 2026
# Version: v1
# Sources Used: W3Schools
# Comments: Simple Calculator made in python, running addition, subtraction, multiplication, division, exponents, and square root
import math
import sys
while True:
    operationQuestion = input("Will you be using Square Root, or another operation? [Square Root (1) | Other Operation (2)] ") # Asking user for square root or another operation
    match operationQuestion:
        case "1": # using square root
            print("Using Square Root")
            SRnum = int(input("What will the number be "))
            SRResult = math.sqrt(SRnum)
            print(f"{SRResult} is your total")
        case "2": # Not using square root
            print("Using another operation")
            num1 = int(input("What will the first number be? "))
            num2 = int(input("What will the second number be? "))
            operationQuestion2 = input("What math operation will you be using? [Addition (1) | Subtraction (2) | Multiplication (3) | Division (4) | Exponents (5)] ") # Asking user what operation to use
            match operationQuestion2:
                case "1": # Using Addition
                    sum = num1 + num2
                    print(f"{sum} is the total")
                case "2": # Using Subtraction
                    sum = num1 - num2
                    print(f"{sum} is the total")
                case "3": # Using Multiplication
                    sum = num1 * num2
                    print(f"{sum} is the total")
                case "4": # Using Division
                    if num2 == 0:
                        print("Error Division By Zero")
                        break
                    sum = num1 / num2
                    print(f"{sum} is the total")
                case "5": # Using Exponents
                    sum = num1 ** num2
                    print(f"{sum} is the total")
        case "quit": # User Quitting
            print("quitting")
            sys.exit(0)
            break
        case _:
            print("Invalid Response")