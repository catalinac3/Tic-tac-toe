from tkinter import *

def setup_game_window():
    '''Setup and layout of the game window'''
    global number_of_players
    global top
    # WINDOW: Game 
    # set up
    message = StringVar()
    top = Toplevel()
    top.title('tic-tac-toe')
    top.geometry("350x350")
    label = Label(top, text="Let's Play")
    back_button = Button(top, text="Back_to_settings",
            padx=5, pady=5, command=to_settings)
    label1 = Label(top, textvariable=message)
    if number_of_players.get()==1:
        message.set(f"welcome player")
    else:
        message.set(f"welcome players")
    #layout
    label.grid(row=0,columnspan=2)
    back_button.grid(row=1,columnspan=2)
    label1.grid(row=2,columnspan=2)

def to_game_window():
    '''calls setup_game_window, and disable buttons in the
     game setting window '''
    setup_game_window()
    # while the game window is on the buttons on 
    # the game settings should be disable.
    start_game['state']=DISABLED
    radio1['state']=DISABLED
    radio2['state']=DISABLED
    entry_names[0]['state']=DISABLED
    entry_names[1]['state']=DISABLED
    
def to_settings():
    '''destroys the game window, activate the choices 
    on the setting window '''
    # when the user goes back to the setting 
    # the buttons on the game settings should be 
    # back to active (normal).
    global top
    top.destroy()
    start_game['state']=NORMAL
    radio1['state']=NORMAL
    radio2['state']=NORMAL
    entry_names[0]['state']=NORMAL
    entry_names[1]['state']=NORMAL

def when_selected():
    '''what is done when a radio button is selected'''
    global number_of_players
    global entry_text
    if number_of_players.get()==1:
        entry_names[1].insert(0,entry_text)
    else:
        # since the whole old text is removed
        # 0 is the start point and END marks wherever 
        # the end currently is.
        entry_names[1].delete(0, END)

    
# WINDOW: Game Settings
win = Tk()

# variable for the radio buttons
number_of_players = IntVar()
# initial value in the radio buttons is 1 player 
# when there is only one player the second entry 
# should be computer
number_of_players.set(1)
entry_text = 'computer'

win.geometry("350x350")
win.title('Tic-tac-toe Game Settings')
lbl1 = Label(win, text="Game Settings")
start_game = Button(win, text="Start-Game",
            padx=5, pady=5, command=to_game_window)
# padx and pady add some extra space between the contents 
# and the button border.
lbl2 = Label(win, text='Choose the number of players')
radio1 = Radiobutton(win, text="1 player",variable=number_of_players, value=1, command=when_selected)
radio2 = Radiobutton(win, text="2 players",variable=number_of_players, value=2, command=when_selected)
lbl_names = []    
entry_names = []
for i in range(2):
    player = i+1
    lbl_name = Label(win, text="Name player " + str(player))
    name_player = Entry(win, width=20, bg='#CCFFFF',
                           borderwidth=3)
    lbl_names.append(lbl_name)
    entry_names.append(name_player)

# since the default is 1 player
# the second entry will be computer
entry_names[1].insert(0,entry_text)

#Layout settings window
lbl1.grid(row=0,columnspan=2)
start_game.grid(row=1,columnspan=2)
lbl2.grid(row=2,columnspan=2)
radio1.grid(row=3, column=0)
radio2.grid(row=3, column=1)
lbl_names[0].grid(row=4, column=0)
entry_names[0].grid(row=4,column=1)
lbl_names[1].grid(row=5, column=0)
entry_names[1].grid(row=5, column=1)

mainloop()

#sticky=W --- to keep text to the left
