# Challenge 3 Starter Code
numbers = []

for i in range(5):
    try:
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    except:
        print("Invalid number. Please enter a numeric value")

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"The sum of the numbers is {total}")
    print(f"The average of the numbers is {average}")
else:
    print("no valid numbers were entered.")

# ---------------- Q & A --------------- #
# A ValueError is caused when the right data tyoe is put in, just is an inappropriate value ex. int("four")
#
# A while loop will loop infinitely until the user stops it, while the for loop is a set amount of loops
#
# Error handling is very important because if even the tiniest mistake is entered, it could break all the code altogether