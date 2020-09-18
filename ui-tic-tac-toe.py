from tkinter import *
from functools import partial

class MainWindow:
    def __init__(self):
        # WINDOW: Game Settings
        # Constructing the Window
        win = Tk()
        win.geometry("350x350")
        win.title('Tic-tac-toe Game Settings') 
        
        self.entry_text = 'computer'    
        self.players = ["player X", "player O"]
        # variable for the radio buttons
        self.number_of_players = IntVar()
        # initial value in the radio buttons is 1 player 
        # when there is only one player the second entry 
        # should be computer
        self.number_of_players.set(1)
        
        lbl1 = Label(win, text="Game Settings")
        lbl2 = Label(win, text='Tic-tac-toe',font='Helvetic 16 bold italic')
        lbl3 = Label(win, text='Choose the number of players')

        # radio1, radio2 and start_game button are disable and enable in other functions
        self.radio1 = Radiobutton(win, text="1 player",variable=self.number_of_players, 
                            value=1,command=self.when_selected)
        self.radio2 = Radiobutton(win, text="2 players",variable=self.number_of_players, 
                            value=2,command=self.when_selected)
        self.start_game = Button(win, text="Start Game",padx=5, pady=5, 
                            command=self.to_game_window)
        # padx and pady add some extra space between the contents 
        # and the button border.

        lbl_names = []     
        self.entry_names = []
        for i in range(2):
            player = i+1
            lbl_name = Label(win, text="Name player " + str(player))
            name_player = Entry(win, width=20, bg='#CCFFFF',
                                borderwidth=3)
            lbl_names.append(lbl_name)
            self.entry_names.append(name_player)

        # since the default is 1 player
        # the second entry will be computer
        self.entry_names[1].insert(0,self.entry_text)

        #Layout settings window
        lbl1.grid(row=0,columnspan=2, padx=10, pady=(10,0))
        lbl2.grid(row=1,columnspan=2, padx=10)
        lbl3.grid(row=2,columnspan=2, padx=10)
        self.radio1.grid(row=3, column=0, padx=10)
        self.radio2.grid(row=3, column=1)
        lbl_names[0].grid(row=4, column=0, padx=10)
        self.entry_names[0].grid(row=4,column=1)
        lbl_names[1].grid(row=5, column=0, padx=10)
        self.entry_names[1].grid(row=5, column=1)
        self.start_game.grid(row=6,columnspan=2, pady=(5,0))

    def when_selected(self):
        '''what is done when a radio button is selected'''
        if self.number_of_players.get()==1:
            self.entry_names[1].delete(0, END)
            self.entry_names[1].insert(0,self.entry_text)
        else:
            # since the whole old text is removed
            # 0 is the start point and END marks wherever 
            # the end currently is.
            self.entry_names[1].delete(0, END)
     
    def set_players(self):
        ''' checks for players input of their name on the interface entry spaces,
        in the case of no inputs, default names: player X and player O, will
        be used during the game'''
        for i in range(2):
            # .get() takes the value on the entry (inserted by the user)
            if len(self.entry_names[i].get()) != 0:
                self.players[i] = self.entry_names[i].get()


    def to_game_window(self):
        '''calls setup_game_window, and disable buttons in the
        game setting window '''
        self.set_players()
        game_window = GameWindow(self.number_of_players, self.players, onclose=self.enable_all)
        # while the game window is on the buttons on 
        # the game settings should be disable.
        self.start_game['state']=DISABLED
        self.radio1['state']=DISABLED
        self.radio2['state']=DISABLED
        self.entry_names[0]['state']=DISABLED
        self.entry_names[1]['state']=DISABLED

    def enable_all(self):
        self.start_game['state'] = NORMAL
        self.radio1['state'] = NORMAL
        self.radio2['state'] = NORMAL
        self.entry_names[0]['state'] = NORMAL
        self.entry_names[1]['state'] = NORMAL

class GameWindow:
    def __init__(self, number_of_players, players, onclose=None):
        self.number_of_players = number_of_players
        self.players = players
        self.onclose = onclose

        # WINDOW: Game 
        self.top = Toplevel()
        self.top.title('tic-tac-toe')
        self.top.geometry("350x350")

        # when closing the top window with x, it will run the function to_settings.
        # same as when the button back to settings is clicked.
        # protocol() --- Registers a callback function for the given protocol. 
        # The name argument is typically one of “WM_DELETE_WINDOW” (the window is about to be deleted)
        self.top.protocol("WM_DELETE_WINDOW", self.to_settings)

        self.message_label4 = StringVar()
        
        label1 = Label(self.top, text='Tic-tac-toe',font='Helvetic 16 bold italic')
        back_button = Button(self.top, text="Back_to_settings",
                padx=5, pady=5, command=self.to_settings)
        label2 = Label(self.top, text=f"{self.players[0]} vs. {self.players[1]}",
                fg = '#1b1c5e', font='Helvetic 12',
                borderwidth=2, relief="groove", padx= 5, pady=5)
        #TO DO --- make the vr. bold
        label3 = Label(self.top, text="Let's Play")
        label4 = Label(self.top, textvariable=self.message_label4, font='TkDefaultFont 10')
        self.message_label4.set(f"This label display the turns")
   
        #layout
        label1.grid(row=0,columnspan=2, padx=10, pady=(20,0))
        label2.grid(row=1,columnspan=2, padx=10)
        label3.grid(row=2,columnspan=2, padx=10)
        label4.grid(row=2,columnspan=2, padx=10)
        back_button.grid(row=3,columnspan=2, padx=10, pady=(5,0))

    def to_settings(self):
        '''destroys the game window, activate the choices 
        on the setting window '''
        # when the user goes back to the setting 
        # the buttons on the game settings should be 
        # back to active (normal).
        self.top.destroy()
        if self.onclose:
            self.onclose()


if __name__ == "__main__":
    main_window = MainWindow()    
    mainloop()

# Extra -----------------------------

# original_font = lbl3.cget('font')
# the original_font is TkDefaultFont




