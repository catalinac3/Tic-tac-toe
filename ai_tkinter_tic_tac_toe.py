# Tic Tac Toe Game

# module for GUI (graphical user interface) Tkinter
import tkinter as tk

# partial to pass functions with arguments activated by buttons
from functools import partial

# random module is imported to handle the computers turn
import random

# Game state (global variables)
count_turns = 0
players = ["player X", "computer"]
# The sets collect the moves of each player
disable_numbers_x = set()
disable_numbers_o = set()


def start():
    ''' Gets the game started. It resets all values stored during the last game.
    This function is called by the start_button
    '''
    global players
    global disable_numbers_x
    global disable_numbers_o
    global count_turns

    # turn counter is reset to cero
    count_turns = 0

    # sets are reset to empty
    disable_numbers_x = set()
    disable_numbers_o = set()

    # buttons of the board games are reset, so that they are available to the
    # players, with no text and in their original color
    for i in range(9):
        if buttons[i]['state'] == 'disabled':
            buttons[i].config(state="normal", text=" ", bg=orig_color)

    message.set(f"It is your turn {players[0]}")


def click_number(i):
    '''Handles first the human turn and then the computer turn by placing an 
    X (for the human turn) and an O (for the computer turn) over a button of the
    game, and disables this button.
    It changes the label in the interface to display if it is the human turn,
    or if there is a winner (this with the function after_player_won()),
    or a tie (in case of no more possible moves).
    Uses the function player_won() for checking if there is a winner.
    This functions is called by pressing any button on the board game

    Parameter:
    i(int): is the number referening the position of the button in the game board
    '''
    global count_turns
    global disable_numbers_x
    global disable_numbers_o

    # Human plays
    buttons[i].config(state="disabled", text='X')
    disable_numbers_x.add(i)
    print(f'x past moves: {disable_numbers_x}')
    current_player = players[0]

    # check if human won
    if player_won(disable_numbers_x, 'playing'):
        after_player_won(current_player)

    elif count_turns == 8:
        message.set(f"It is a tie")
    else:
        message.set(f"It is your turn {players[0]}")
    count_turns += 1

    # Computer playes
    current_player = players[1]
    disable_numbers_o_copy = disable_numbers_o.copy()
    disable_numbers_x_copy = disable_numbers_x.copy()
    move = deciding_computer_move(
        disable_numbers_o_copy, disable_numbers_x_copy)
    buttons[move].config(state="disabled", text='O')
    disable_numbers_o.add(move)

    # Check if computer won
    if player_won(disable_numbers_o, 'playing'):
        after_player_won(current_player)
    # There is no check for a tie, because the human is the last to play

    count_turns += 1


def after_player_won(current_player):
    '''Once a player has won, changes the label to celebrate it and
    dissables all the buttons on the board game.
    Parameters:
    current_player(str)
    Return:
    move(int): position on the tic-tac-toe board
    '''

    message.set(f"{current_player} won!! :) ")
    # this code disable left over buttons after winning
    for i in range(9):
        if buttons[i]['state'] == 'normal':
            buttons[i].config(state="disabled", text=" ")


def deciding_computer_move(disable_numbers_o_copy, disable_numbers_x_copy):
    '''In this function the computer decides the next move
    Parameters:
    disable_numbers_o_copy(set): copy of the moves up to this moment of the computer
    disable_numbers_x_copy(set): copy of the moves up to this moment of the player
    Return
    move(int): position on the board
    '''
    available_moves = []
    for i in range(9):
        if buttons[i]['state'] == 'normal':
            available_moves.append(i)
    print(available_moves)

    # Check if computer can win with the next move
    for i in available_moves:
        disable_numbers_o_copy.add(i)
        if player_won(disable_numbers_o_copy):
            move = i
            return move
        disable_numbers_o_copy.remove(i)

    # Check if the human can win with the next move
    for i in available_moves:
        disable_numbers_x_copy.add(i)
        if player_won(disable_numbers_x_copy):
            move = i
            return move
        disable_numbers_x_copy.remove(i)

    # Check if any of the corners and center are available to make a move
    # Center and corners are python-positions [0,2,6,8,4] in the board
    corners_center_available = []
    for i in available_moves:
        if i in [0, 2, 4, 6, 8]:
            corners_center_available.append(i)
    move = random.choice(corners_center_available)

    if move:
        return move

    # Check if any of the sides are available to make a move
    # Center and corners are python positions [1,3,5,7] in the board
    sides_available = []
    for i in available_moves:
        if i in [1, 3, 5, 7]:
            sides_available.append(i)
    move = random.choice(sides_available)

    if move:
        return move


def player_won(check_disable, game_state='trying'):
    '''Checks if the last player to make a move has won, when a player has won
    the buttons with the winning three in a row will turn to a color blue

    Parameter:
    check_disable(set): collected moves of the last player to make a move
    game_state(str): 'trying': default values, indicates computer is checking
                               if he or the human can win.
                     'playing': indicates real win
    Returns:
    (bool): True if the player won or False if no player has won
    '''

    win_combinations = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                        {2, 4, 6}, {0, 4, 8}]
    for win_set in win_combinations:
        if win_set.issubset(check_disable):
            if game_state == "playing":
                for elem in win_set:
                    buttons[elem]['bg'] = '#CCFFFF'
                return True
            elif game_state == 'trying':
                return True
    return False


# Main code
# All functions above will be called by the buttons bellow
win = tk.Tk()

# It determines how big the screen is
win.geometry("300x200")

win.title('Tic-tac-toe game')


heading_font = 'Helvetica'

# Dinamic label in the code, it will update itself according to the set message
message = tk.StringVar()
label_2 = tk.Label(
    win, textvariable=message)
label_2.grid(row=1, column=4, columnspan=4, rowspan=2)

message.set("Let's play!")

# This button starts the game
start_button = tk.Button(win, text="Click here to start",
                         padx=5, pady=5, command=start)
start_button.grid(row=1, column=4, columnspan=2)

# These buttons are the board of the the game
size_font = 20
buttons = []
for i in range(9):
    button = tk.Button(win, text=' ',
                       command=partial(click_number, i),
                       font=(heading_font, size_font), width=3)
    button.grid(row=i//3, column=i % 3)
    buttons.append(button)
orig_color = button.cget("background")
# orig_color is SystemButtonFace


win.mainloop()
