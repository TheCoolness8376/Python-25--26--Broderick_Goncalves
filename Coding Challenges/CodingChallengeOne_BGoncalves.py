# Challenge 1 Starter Code
name = "Brody"
age = 16
height = 1.9

print(f"Hi! My name is {name} and I'm {age} years old. I'm {height} meters tall.")
print(type(name))
print(type(age))
print(type(height))

# Q & A
# 1. Int has no decimal places, while float does. Ex. int would be 8, float would be 8.0
# 2. Python doesn't require variable type declarations because of dynamic typing and easy readability
# 3. If age was set to a string, the number would have to be put in quotation marks, and would't be able to have any math don to the number because it's not an int. Also, the type would say that age is a string

# ---------- Modding ---------- #
nameQuestion = input("What is your name? ")
ageQuestion = input("How old are you? ")
heightQuestion = input("How tall are you in meters? ")
print("Your name is: " + nameQuestion.upper())
print(f"You are {age} years old")
print(f"You are {height} meters tall")