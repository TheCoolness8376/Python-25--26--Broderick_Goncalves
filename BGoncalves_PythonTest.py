# PYTHON-Test-1-Challenge-2-Banking-System-Simulator
# Python - Test 1 covers Lectures 1 to 4
# Covers:
# Variables, Loops, Conditionals, Functions, Error Handling
# 🎯 Goal
# Simulate a simple bank account.
# 🧩 Requirements
# Start with a balance of 0.
# Create functions:
# deposit(balance, amount)
# withdraw(balance, amount)
# Use a loop to display a menu:
# 1 → Deposit
# 2 → Withdraw
# 3 → Check Balance
# 4 → Exit
# Prevent withdrawing more than the balance.
# Handle invalid inputs using try/except.
# Track total number of transactions.
# 🚀 Bonus
# Add transaction fees ($1 per withdrawal)
# Prevent negative deposits

# Brody Goncalves
# 2 / 26 / 2026
# v1
# Sources Used: CoPilot
# Comments: Simple banking system simulator that allows users to deposit, withdraw, check balance, and exit. It includes error handling for invalid inputs and prevents overdrawing the account.

def deposit(balance, amount):
    if amount < 0:
        print("Cannot deposit a negative value.")
        return balance
    return balance + amount

def withdraw(balance, amount):
    if amount + 1 > balance: # $1 trasaction fee
        print ("Insufficient funds for withdrawal inclluding transaction fee.")
        return balance
    return balance - amount - 1 # $1 transaction fee

def main():
    balance = 0
    transactions = 0
    
    while True:
        print("\nMenu:")
        print("1 → Deposit")
        print("2 → Withdraw")
        print("3 → Check Balance")
        print("4 → Exit")
        choice = input("Choose an option: ")

        try:
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                balance = deposit(balance, amount)
                transactions += 1
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                balance = withdraw(balance, amount)
                transactions += 1
            elif choice == '3':
                print(f"Current balance: ${balance:.2f}")
            elif choice == '4':
                print(f"Total transactions: {transactions}")
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()