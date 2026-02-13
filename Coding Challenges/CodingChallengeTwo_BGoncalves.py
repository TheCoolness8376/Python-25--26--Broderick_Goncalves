# Challenge 2 Starter Code
user_input = input("Enter a word: ")
if len(user_input) > 5:
    print("Your word is a Long Word")
else:
    print("Your word is a Short Word")
print("Your word is: " + user_input.lower())
print("Your word is: " + user_input.upper())
wordLength = len(user_input)
print(f"The length of your word is: {wordLength}")

# ---------- Q & A ---------- #
# 1. len() returns the length of the word thats inputted
# 2. Input must be cast first before math operations to get the users number input
# 3. == checks for equality