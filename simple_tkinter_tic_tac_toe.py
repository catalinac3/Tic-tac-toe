# Tic Tac Toe Game

# module for GUI (graphical user interface) Tkinter
import tkinter as tk

# partial to pass functions with arguments activated by buttons
from functools import partial

# Game state (global variables)
count_turns = 0
players = ["player X", "player O"]
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
    '''Places an X or an O over the pressed button of the game and disable this 
    button. It changes the label to display who's next,checks if there is a 
    winner using the function player_won() or if there is no more possible moves. 
    Once a player has won, it dissables all the buttons on the board game.
    This functions is called by pressing any button on the board game

    Parameter:
    i(int): is the number referening the position of the button in the game board
    '''
    global count_turns
    global disable_numbers_x
    global disable_numbers_o

    if count_turns % 2 == 0:
        current_player = players[0]
        buttons[i].config(state="disabled", text='X')
        next_player = players[1]
        disable_numbers_x.add(i)
        check_disable = disable_numbers_x
    else:
        current_player = players[1]
        buttons[i].config(state="disabled", text='O')
        next_player = players[0]
        disable_numbers_o.add(i)
        check_disable = disable_numbers_o
    count_turns += 1

    if player_won(check_disable):
        message.set(f"{current_player} won!! :) ")

        # this code disable left over buttons after winning
        for i in range(9):
            if buttons[i]['state'] == 'normal':
                buttons[i].config(state="disabled", text=" ")
    elif count_turns == 9:
        message.set(f"It is a tie")
    else:
        message.set(f"Your turn {next_player}")


def player_won(check_disable):
    '''Checks if the last player to make a move has won, when a player has won 
    the buttons with the winning three in a row will turn to a color blue

    Parameter:
    check_disable(set): collected moves of the last player to make a move
    Returns:
    (bool): True if the player won or False if no player has won
    '''
    win_combinations = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                        {2, 4, 6}, {0, 4, 8}]
    for win_set in win_combinations:
        if win_set.issubset(check_disable):
            for elem in win_set:
                buttons[elem]['bg'] = '#CCFFFF'
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
