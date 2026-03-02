# Brody Goncalves
#  /  / 26
# v1
# Copilot
# Comments:
# - This is rock, paper, scissors, but, this version sees how many you can get right in a row
# - All you have to do is choose 0 - 3 (rock, paper, scissors, and quit) and everything else is done for you

import random

points = 0

print("\n\nWelcome to Rock, Paper, Scissors! (You can quit at ant time with 0)")

while True:
    randNum = random.randint(0, 2)
    try:
        roPapSci = input("\nRock [1], Paper [2], Scissors [3], or Quit [0]? ")
    except:
        print("Invalid input. Please enter a number (0-3).")
        continue

    if (roPapSci == 1):
        match (randNum):
            case 0:
                print("draw \nTotal points = " + points + "\nCurrent Highscore: " + loadHighscore())
                break
            case 1:
                print("Paper beats rock! You lose. Winstreak is now ded \nYour score was " + points + "\nResetting score")
                points = 0
                break
            case 2:
                print("Rock beats Scissors! You win!")