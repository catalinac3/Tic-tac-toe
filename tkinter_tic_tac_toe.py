# Tic Tac Toe Game

# module for GUI (graphical user interface) Tkinter
import tkinter as tk

# partial to pass functions with arguments activated by buttons
from functools import partial

# Game state (global variables)
count_turns = 0
players = ["player X", "player O"]
disable_numbers_x = set()
disable_numbers_o = set()


# TODO
def play():
    '''This functions gets activated when the button click to start is clicked '''
    global players
    global disable_numbers_x
    global disable_numbers_o
    global count_turns

    count_turns = 0

    # here the sets that collect the moves of each players are reseted
    disable_numbers_x = set()
    disable_numbers_o = set()

    # This code reset the buttons of the board, the availability, text, and color
    for i in range(9):
        if buttons[i]['state'] == 'disabled':
            buttons[i].config(state="normal", text=" ", bg=orig_color)

    # This loop checks for players input of their name in case of no inputs,
    # it uses the default values names: player X and player O.
    for i in range(2):
        # .get() takes the value on the entry (inserted by the user)
        if len(entries_name[i].get()) != 0:
            players[i] = entries_name[i].get()

    message.set(
        f"Welcome players: {players[0]} & {players[1]},\n it's your turn {players[0]}")


def click_number(i):
    '''This function place an X or an O over the pressed button and disable
    this button in the game board. It changes the label to display who's next,
    checks if there is a winner or if there is no more moves.
    All once a button in the board game is clicked '''
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
    '''This function returns True: if the player won OR False: if no player
    hat yet won'''
    win_combinations = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                        {2, 4, 6}, {0, 4, 8}]
    for win_set in win_combinations:
        if win_set.issubset(check_disable):
            for elem in win_set:
                buttons[elem]['bg'] = '#CCFFFF'
            return True

    return False


# All functions above will be called by the buttons bellow
# Making a GUI with Tkinter for the tic-tac-toe game
win = tk.Tk()

# It determines how big the screen is
win.geometry("350x350")

win.title('Tic-tac-toe game')


heading_font = 'Helvetica'
label_1 = tk.Label(win, text="Let's play",
                   font=heading_font).grid(row=0, column=1)

# This code makes the two labels and entries for the name of the player
entries_name = []
row_place = 1
for i in range(2):
    player = i+1
    tk.Label(win, text="Name player "+str(player)).grid(row=row_place)
    name_player = tk.Entry(win, width=20, bg='#CCFFFF',
                           borderwidth=3)
    name_player.grid(row=row_place, column=1)
    entries_name.append(name_player)

    row_place += 1

# This label will update itself according to the set message
message = tk.StringVar()
label_2 = tk.Label(
    win, textvariable=message)
label_2.grid(row=4, column=0, columnspan=4, rowspan=2)

# These buttons here are the board of the the game
# They are located in a different frame call Game_frame
size_font = 20
Game_frame = tk.Frame(win)
Game_frame.grid(row=6, column=1)
buttons = []
for i in range(9):
    button = tk.Button(Game_frame, text=' ',
                       command=partial(click_number, i),
                       font=(heading_font, size_font), width=3)
    button.grid(row=i//3, column=i % 3)
    buttons.append(button)
orig_color = button.cget("background")
# orig_color is SystemButtonFace

# This button starts the game
tk.Button(win, text="Click here to start",
          padx=5, pady=5, command=play).grid(row=3, columnspan=2)

win.mainloop()

# Useful references:
# https://www.geeksforgeeks.org/python-gui-tkinter/
# http://effbot.org/tkinterbook/label.htm
