# ---------- Practice Activity 1 ---------- #
import math

num = int(input("Enter a number: "))
answer = math.sqrt(num)
print(f"The square root of {num} is {answer}")

# ---------- Practice Activity 2 ---------- #
name = input("What is your name? ")
for i in range(len(name)):
    print(name[i])

# ---------- Practice Activity 3 ---------- #
import random
num1 = random.randint(1, 15)
num2 = random.randint(1, 15)
print(f"You got a {num1} and a {num2}")