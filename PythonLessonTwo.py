word = "Python"
print(word[0]) # Will print P

word2 = "Python"
print(len(word)) # Will print 6

val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")
# For both of these, where the curly brackets are with the variable,
# it replaces with the String or int when printed

day = 1
match day: # <---- match is the pythonn switch
    case 1:
        print("Monday")
    case _: # <---- _ is the default of python
        print("Invalid day")

# If statements are if / elif / else

# ---------- Practice Activity ---------- #

choice = int(input("Choose option: (1 - Start | 2 - Exit) "))
match choice:
    case 1:
        print("Starting")
    case 2:
        print("Exiting")
    case _:
        print("Invalid choice")
name = input("What is your name? ")
age = int(input("How old are you? "))
if age <= 17:
    print(f"So your name is {name} and you're {age} years old, or a minor")
elif age <= 20 and age >= 18:
    print(f"So your name is {name} and you're {age} years old, or a young adult")
elif age >= 21:
    print(f"So your name is {name} and you're {age} years old, or an adult")
else:
    print("Invalid Response")