from tkinter import *

def to_game_window():
    global top
    global player_number
    message = StringVar()
    top = Toplevel()
    top.title('tic-tac-toe')
    top.geometry("350x350")
    label = Label(top, text="you are in the game window")
    back_button = Button(top, text="Back_to_settings",
            padx=5, pady=5, command=to_settings)
    # while the game window is on the buttons on 
    # the game settings should be disable.
    start_game['state']=DISABLED
    radio_1['state']=DISABLED
    radio_2['state']=DISABLED
    
    label1 = Label(top, textvariable=message)
    if player_number.get()==1:
        message.set(f"welcome player")
    else:
        message.set(f"welcome players")

    #layout
    label.grid(row=0,columnspan=2)
    back_button.grid(row=1,columnspan=2)
    label1.grid(row=2,columnspan=2)

def to_settings():
    # when the user goes back to the setting 
    # the buttons on the game settings should be 
    # back to active (normal).
    global top
    top.destroy()
    start_game['state']=NORMAL
    radio_1['state']=NORMAL
    radio_2['state']=NORMAL
    

    

win = Tk()
#variable for the radio buttons
player_number = IntVar()
# player_number.get() --- to use this variable
win.geometry("350x350")
win.title('Tic-tac-toe Game Settings')
lbl1 = Label(win, text="Game Settings")
start_game = Button(win, text="Start-Game",
            padx=5, pady=5, command=to_game_window)
# padx and pady add some extra space between the contents 
# and the button border.
lbl2 = Label(win, text='Choose the number of players')
radio_1= Radiobutton(win, text="1 player",variable=player_number, value=1)
radio_2= Radiobutton(win, text="2 player",variable=player_number, value=2)

#Layout settings window
lbl1.grid(row=0,columnspan=2)
start_game.grid(row=1,columnspan=2)
lbl2.grid(row=2,columnspan=2)
radio_1.grid(row=3, column=0)
radio_2.grid(row=3, column=1)


#sticky=W --- to keep text to the left
mainloop()

