# Brody Goncalves
# 2 / 22 / 26
# v1
# Sources Used: None
# This number guessing game features 3 difficulties
# This simple number game lets you "gamble" your luck with guessing numbers
import sys
import random
while True:
    difficultyQuestion = input("\nChoose your difficulty (easy, normal, hard, quit) ")
    match difficultyQuestion:
        case "easy": # EASY Difficulty
            print("\nLet's go gambling!!!\nYou have 15 tries...Ready...Go!")
            easyRandNum = random.randint(0, 50)
            easyAttempts = 14
            easyGuess = 0
            while (easyGuess != easyRandNum and easyAttempts > -1):
                easyNumGuess = int(input("\nGuess a number between 0 and 50: "))
                if (easyNumGuess != easyRandNum and easyAttempts == 0): # No attempts left
                    print(f"The number was {easyRandNum}")
                    break
                if easyNumGuess < easyRandNum: # Guess too low
                    print(f"Too low. Guess higher.\nYou have {easyAttempts} tries left")
                    easyAttempts -= 1
                elif easyNumGuess > easyRandNum: # Guess too high
                    print(f"Too high. Guess lower.\nYou have {easyAttempts} tries left")
                    easyAttempts -= 1
                else: # Correct Guess
                    print(f"You Win!\nYou had {easyAttempts} tries left")
                    break
        case "normal": # NORMAL Difficulty
            print("\nLet's go gambling!!!\nYou have 10 tries...Ready...Go!")
            normRandNum = random.randint(0, 75)
            normAttempts = 9
            normGuess = 0
            while (normGuess != normRandNum and normAttempts > -1):
                normNumGuess = int(input("\nGuess a number between 0 and 75: "))
                if (normNumGuess != normRandNum and normAttempts == 0): # No attempts left
                    print(f"The number was {normRandNum}")
                    break
                if normNumGuess < normRandNum: # Guess too low
                    print(f"Too low. Guess higher.\nYou have {normAttempts} tries left")
                    normAttempts -= 1
                elif normNumGuess > normRandNum: # Guess too high
                    print(f"Too high. Guess lower.\nYou have {normAttempts} tries left")
                    normAttempts -= 1
                else: # Correct Guess
                    print(f"You Win!\nYou had {normAttempts} tries left")
                    break
        case "hard": # HARD Difficulty
            print("\nLet's go gambling!!!\nYou have 5 tries...Ready...Go!")
            hardRandNum = random.randint(0, 100)
            hardAttempts = 4
            hardGuess = 0
            while (hardGuess != hardRandNum and hardAttempts > -1):
                hardNumGuess = int(input("\nGuess a number between 0 and 100: "))
                if (hardNumGuess != hardRandNum and hardAttempts == 0): # No attempts left
                    print(f"The number was {hardRandNum}")
                    break
                if hardNumGuess < hardRandNum: # Guess too low
                    print(f"Too low. Guess higher.\nYou have {hardAttempts} tries left")
                    hardAttempts -= 1
                elif hardNumGuess > hardRandNum: # Guess too high
                    print(f"Too high. Guess lower.\nYou have {hardAttempts} tries left")
                    hardAttempts -= 1
                else: # Correct Guess
                    print(f"You Win!\nYou had {hardAttempts} tries left")
                    break
        case "quit": # User Quits
            print("quitting")
            sys.exit(0)
            break
        case _: # User has an invalid response
            print("Invalid Response")