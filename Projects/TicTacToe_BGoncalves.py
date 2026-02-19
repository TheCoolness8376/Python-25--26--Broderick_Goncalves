# Brody Goncalves
# 2 / 22 / 26
# v1
# Sources Used: CoPilot
# How to use:
# - Player 1 chooses either 'X' or 'O'. Players take turns entering
#   a number 1-9 to place their marker. The game reports wins or ties
#   and asks whether to play again.

import random

def display_board(board):
    # We draw a 3x3 layout so players can see the current state.
    # We'll display as 1-9 positions in the standard reading order (1..9).
    print()
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print()


def player_input():
    # Ask Player 1 to choose their marker 'X' or 'O'.    
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1: Do you want to be X or O? ").upper()
    # Assign the opposite marker to Player 2
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    # Place the player's marker on the board at the given position.
    board[position] = marker


def win_check(board, mark):
    # Check whether the given mark has a winning combination on the board.
    # Returns True if the mark occupies any row, column or diagonal.
    return ((board[1] == board[2] == board[3] == mark) or  # top row
            (board[4] == board[5] == board[6] == mark) or  # middle row
            (board[7] == board[8] == board[9] == mark) or  # bottom row
            (board[1] == board[4] == board[7] == mark) or  # left col
            (board[2] == board[5] == board[8] == mark) or  # middle col
            (board[3] == board[6] == board[9] == mark) or  # right col
            (board[1] == board[5] == board[9] == mark) or  # diag
            (board[3] == board[5] == board[7] == mark))    # diag


def choose_first():
    # Randomly choose which player goes first. Returns the string 'Player 1' or 'Player 2'.
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    # Return True if the given board position is free (not occupied). Positions are 1-9.
    return board[position] == ' '


def full_board_check(board):
    # Return True if every position on the board is filled.
    # Used to detect a tie (draw) when no win has occurred.
    # If any space is free, board is not full
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board, player_name):
    #  a player for their next move (1-9) and validate it.
    # Keeps prompting until a valid free position integer is entered.
    position = 0
    while True:
        choice = input(f"{player_name}, choose your next position (1-9): ")
        # Validate numeric input
        if not choice.isdigit():
            print('Please enter a number between 1 and 9.')
            continue
        position = int(choice)
        # Validate range and availability
        if position not in range(1, 10):
            print('Invalid position. Choose a number 1-9.')
            continue
        if not space_check(board, position):
            print('That space is already taken. Choose another.')
            continue
        break
    return position


def replay():
    # Ask the players whether they want to play again.
    return input('Do you want to play again? Enter Yes or No: ').strip().lower().startswith('y')


def main():
    #  game loop: sets up the game and alternates turns until end.
    # This function coordinates the players, checks for wins/ties, and
    # offers the option to play again.
    
    print('Welcome to Tic Tac Toe!')

    while True:
        # Create an empty board (index 0 unused for convenience)
        board = [' '] * 10

        # Let Player 1 choose marker and assign the other to Player 2
        player1_marker, player2_marker = player_input()

        # Randomly decide who goes first
        turn = choose_first()
        print(turn + ' will go first.')

        game_on = True

        # While the game is active, alternate turns
        while game_on:
            if turn == 'Player 1':
                # Show board and ask Player 1 for a move
                display_board(board)
                position = player_choice(board, 'Player 1')
                place_marker(board, player1_marker, position)

                # Check if Player 1 has won after their move
                if win_check(board, player1_marker):
                    display_board(board)
                    print('Congratulations! Player 1 has won the game!')
                    game_on = False
                else:
                    # If the board is full and no winner, it's a tie
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a tie!')
                        break
                    else:
                        # No win or tie; switch to Player 2
                        turn = 'Player 2'

            else:  # Player 2's turn
                display_board(board)
                position = player_choice(board, 'Player 2')
                place_marker(board, player2_marker, position)

                if win_check(board, player2_marker):
                    display_board(board)
                    print('Player 2 has won! Well played!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'

        # Ask whether to play again; if not, break the outer loop
        if not replay():
            print('Thanks for playing Tic Tac Toe! Goodbye.')
            break


if __name__ == '__main__':
    main()
