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
    ''' Gets the game started. It resets all values stored during the last game
    and deals with the name input of the players. This function is called by 
    the start_button
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

    # checks for players input of their name on the interface entry spaces,
    # in the case of no inputs, default names: player X and player O, will
    # be used during the game
    for i in range(2):
        # .get() takes the value on the entry (inserted by the user)
        if len(entries_name[i].get()) != 0:
            players[i] = entries_name[i].get()

    message.set(
        f"Welcome players: {players[0]} & {players[1]},\n it's your turn {players[0]}")

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


# All functions above will be called by the buttons bellow
# Making a GUI with Tkinter for the tic-tac-toe game
win = tk.Tk()

# It determines how big the screen is
win.geometry("350x350")

win.title('Tic-tac-toe game')


heading_font = 'Helvetica'

# Static label at the top of the GUI
label_1 = tk.Label(win, text="Let's play",
                   font=heading_font).grid(row=0, column=1)

# Makes the a labels and an entries for each of the players to collect the name
# of the players
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

# Dinamic label in the code, it will update itself according to the set message
message = tk.StringVar()
label_2 = tk.Label(
    win, textvariable=message)
label_2.grid(row=4, column=0, columnspan=4, rowspan=2)

# These buttons are the board of the the game
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
start_button = tk.Button(win, text="Click here to start",
                         padx=5, pady=5, command=start)
start_button.grid(row=3, columnspan=2)

win.mainloop()
