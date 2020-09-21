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
        self.start_game = Button(win, text="Start game",padx=5, pady=5, 
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
        lbl1.grid(row=0,columnspan=2, padx=90, pady=(50,0))
        lbl2.grid(row=1,columnspan=2, padx=90)
        lbl3.grid(row=2,columnspan=2, padx=90)
        self.radio1.grid(row=3, column=0, padx=20, sticky=E)
        self.radio2.grid(row=3, column=1, padx=20, sticky=W)
        lbl_names[0].grid(row=4, column=0, padx=15, pady=(4,0), sticky=E)
        self.entry_names[0].grid(row=4,column=1, pady=(4,0), sticky=W)
        lbl_names[1].grid(row=5, column=0, padx=15, pady=(4,0), sticky=E)
        self.entry_names[1].grid(row=5, column=1, pady=(4,0), sticky=W)
        self.start_game.grid(row=6,columnspan=2, pady=(15,0))

    def when_selected(self):
        '''when 1player is selected on the radio button, 
        computer is use as a name for the second player, 
        otherwise both spaces are blank to fill'''
        if self.number_of_players.get()==1:
            self.entry_names[1].delete(0, END)
            self.entry_names[1].insert(0,self.entry_text)
        else:
            # since the whole old text is removed
            # 0 is the start point and END marks wherever 
            # the end currently is.
            self.entry_names[1].delete(0, END)
     
    def set_players(self):
        '''checks for players name input on the entry spaces,
        in the case of no inputs, the default names are: player X and player O'''
        for i in range(2):
            # .get() takes the value on the entry (inserted by the user)
            if len(self.entry_names[i].get()) != 0:
                self.players[i] = self.entry_names[i].get()


    def to_game_window(self):
        '''sets the game window, and disable all the buttons 
        of the game setting window '''
        self.set_players()
        GameWindow(self.number_of_players,
                   self.players, onclose=self.enable_all)
        # while the game window is on the buttons on 
        # the game settings should be disable.
        self.start_game['state']=DISABLED
        self.radio1['state']=DISABLED
        self.radio2['state']=DISABLED
        self.entry_names[0]['state']=DISABLED
        self.entry_names[1]['state']=DISABLED

    def enable_all(self):
        '''enable all the buttons in the game setting window '''
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
        # width*height
        self.top.geometry("700x350")

        # when closing the top window with x, it will run the function to_settings.
        # same as when the button back to settings is clicked.
        # protocol() --- Registers a callback function for the given protocol. 
        # The name argument is typically one of “WM_DELETE_WINDOW” (the window is about to be deleted)
        self.top.protocol("WM_DELETE_WINDOW", self.to_settings)

        self.message_label4 = StringVar()
        
        label1 = Label(self.top, text='Tic-tac-toe',font='Helvetic 16 bold italic')
        back_button = Button(self.top, text="Back to settings",
                padx=5, pady=5, command=self.to_settings)
        label2 = Label(self.top, text=f"{self.players[0]} vs. {self.players[1]}",
                fg = '#1b1c5e', font='Helvetic 12',
                borderwidth=2, relief="groove", padx= 5, pady=5)
        #TO DO --- make the vr. bold
        label3 = Label(self.top, text="Let's Play")
        label4 = Label(self.top, textvariable=self.message_label4, font='TkDefaultFont 10')
        self.message_label4.set(f"This label display the turns")

        #Game frame
        Game_frame = Frame(self.top)
       
        game_btns = []
        for i in range(9):
            game_btn = Button(Game_frame, text=' ',
                            command=partial(self.click_number, i),
                            font=('Helvetica', 20), width=3)
            game_btn.grid(row=i//3, column=i%3)
            game_btns.append(game_btn)
        

        #Play again button
        play_again_btn = Button(self.top, text="Play again",
                         padx= 5, pady=5, command=self.start)
        
        #layout
        label1.grid(row=0, column=0, columnspan=2, padx=80, pady=(10,0))
        label2.grid(row=1, column=0, columnspan=2, padx=80)
        label3.grid(row=2, column=0, columnspan=2, padx=80)
        label4.grid(row=3, column=0, columnspan=2, padx=80)
        Game_frame.grid(row=4, column=0, columnspan=2, padx=80)
        play_again_btn.grid(row=5, column=0, padx= 5, pady=(5,0), sticky=E)
        back_button.grid(row=5, column=1, padx=5, pady=(5,0), sticky=W)
        
    def to_settings(self):
        '''destroys the game window and activate the choices 
        on the setting window '''
        # when the user goes back to the setting 
        # the buttons on the game settings should be 
        # back to active (normal).
        self.top.destroy()
        if self.onclose:
            # the onclose() is calling the function enable_all from 
            # class MainWindow, used in the constructor
            # of the gameWindow object.
            self.onclose()

    def click_number(self):
        pass

    def start(self):
        pass

if __name__ == "__main__":
    main_window = MainWindow()    
    mainloop()

# Extra -----------------------------

# original_font = lbl3.cget('font')
# the original_font is TkDefaultFont

# orig_color = button.cget("background")
# orig_color is SystemButtonFace



