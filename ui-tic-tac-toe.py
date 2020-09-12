from tkinter import *

def to_game_window():
    '''by pressing the button the window will be destroyed'''
    top = Toplevel()
    top.title('tic-tac-toe')
    top.geometry("350x350")
    lbl = Label(top, text="you are in the game window")
    lbl.pack()
    back_button = Button(top, text="Back_to_settings",
            padx=5, pady=5, command=top.destroy)
    back_button.pack()

win = Tk()
win.geometry("350x350")
win.title('Tic-tac-toe Game Settings')
start_game = Button(win, text="Start-Game",
            padx=5, pady=5, command=to_game_window)
# padx and pady add some extra space between the contents 
# and the button border.

start_game.pack()

mainloop()