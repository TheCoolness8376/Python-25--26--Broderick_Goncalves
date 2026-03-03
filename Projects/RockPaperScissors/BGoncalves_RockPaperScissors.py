# Brody Goncalves
# 3 / 8 / 26
# v1
# Copilot
# Comments:
# - This is rock, paper, scissors, but, this version sees how many you can get right in a row
# - All you have to do is choose 0 - 3 (rock, paper, scissors, and quit) and everything else is done for you

import random
import sys

points = 0
HIGHSCORE_FILE = 'highscore.txt'

def getHighscoreFile():
    return HIGHSCORE_FILE

def resetHighscore():
    try:
        with open(getHighscoreFile(), "w") as writer:  # "w" = overwrite mode
            writer.write("0")
            writer.flush()  # optional, happens automatically on close
    except OSError as e:  # OSError covers file-related errors in Python
        print(f"Error resetting highscore: {e}", file=sys.stderr)

def saveHighscore(highscore):
    try:
        with open(getHighscoreFile(), "w") as writer:  # "w" = overwrite
            writer.write(str(highscore))  # convert to string like String.valueOf()
            writer.flush()  # optional (auto when exiting "with")
    except OSError as e:
        print(f"Error saving highscore: {e}", file=sys.stderr)

def loadHighscore():
    highscore = 0
    try:
        with open(getHighscoreFile(), "r") as reader:
            line = reader.readline()
            if line and line.strip():
                return int(line.strip())
    except FileNotFoundError:
        # File doesn't exist yet — that's fine
        return 0
    except ValueError as e:
        print(f"Invalid highscore format in file: {e}", file=sys.stderr)
    except OSError as e:
        print(f"Error loading highscore: {e}", file=sys.stderr)
    return highscore

print("\n\nWelcome to Rock, Paper, Scissors! (You can quit at any time with 0)") # Intro

try:
    while True:
        randNum = random.randint(0, 2) # Computer choosing Rock, Paper, or Scissors
        try:
            roPapSci = int(input("\nRock [1], Paper [2], Scissors [3], or Quit [0]? ")) # User choosing Rock, Paper, or Scissors
        except:
            print("Invalid input. Please enter a number (0-3).")
            continue

        if (roPapSci == 1): # User selects Rock
            match (randNum):
                case 0: # Computer chooses Rock
                    print(f"draw \nTotal points = {points} \nCurrent Highscore: {loadHighscore()}")
                case 1: # Computer Chooses Paper
                    print(f"Paper beats rock! You lose. Winstreak is now ded \nYour score was {points} \nResetting score")
                    points = 0               
                case 2: # Computer Chooses Scissors
                    print("Rock beats Scissors! You win!")
                    points += 1
                    stored = loadHighscore()
                    if (points > stored):
                        saveHighscore(points)
                    print(f"You win! +1 point! \nTotal points = {points} \nCurrent Highscore: {loadHighscore()}")
                    
        if (roPapSci == 2): # User selects Paper
            match (randNum):
                case 0: # Computer chooses Rock
                    print("Paper beats rock! You win!")
                    points += 1
                    stored = loadHighscore()
                    if (points > stored):
                        saveHighscore(points)
                    print(f"You win! +1 point!\nTotal points = {points} \nCurrent Highscore: {loadHighscore()}")               
                case 1: # Computer Chooses Paper
                    print(f"draw \nTotal points = {points} \nCurrent Highscore: {loadHighscore()}")              
                case 2: # Computer Chooses Scissors
                    print(f"Scissors beats paper! You lose. Winstreak is now ded \nYour score was {points} \nResetting score")
                    points = 0
                    
        if (roPapSci == 3): # User selects Scissors
            match (randNum):
                case 0: # Computer chooses Rock
                    print("Rock beats Scissors! You lose. Winstreak is now ded")
                    print(f"Your score was {points} \nResetting score")
                    points = 0             
                case 1: # Computer Chooses Paper
                    print("Scissors beats paper! You win!")
                    points += 1
                    stored = loadHighscore()
                    if (points > stored):
                        saveHighscore(points)
                    print(f"You win! +1 point!\nTotal points = {points} \nCurrent Highscore: {loadHighscore()}")           
                case 2: # Computer Chooses Scissors
                    print(f"draw \nTotal points = {points} \nCurrent Highscore: {loadHighscore()}")
                    
        elif (roPapSci == 0): # User selects quit
            print("Quitting. Goodbye!")
            # save current points as highscore if it's greater than stored
            try:
                stored = loadHighscore()
                if points > stored:
                    saveHighscore(points)
            except Exception:
                pass
            sys.exit(0)
except (KeyboardInterrupt, SystemExit):
    # ensure highscore is saved on Ctrl-C or sys.exit
    try:
        stored = loadHighscore()
        if points > stored:
            saveHighscore(points)
    except Exception:
        pass
    raise
finally:
    # final safety save for any other unexpected exit
    try:
        stored = loadHighscore()
        if points > stored:
            saveHighscore(points)
    except Exception:
        pass