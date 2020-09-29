from tkinter import *
from functools import partial
import random

class GameWindow:
    def __init__(self, number_of_players, players, onclose=None):
        self.number_of_players = number_of_players
        self.players = players
        self.onclose = onclose

        self.count_turns = 0
        self.disable_numbers_x = set()
        self.disable_numbers_o = set()

        # The first time that someone plays goes directly to the board
        # This code sorts out who will be starting the game
        random.shuffle(self.players)
        self.player_x = self.players[0]
        self.player_o = self.players[1]
        
        # WINDOW: Game 
        self.top = Toplevel()
        self.top.title('tic-tac-toe')
        # Width*height
        self.top.geometry("700x350")

        # When closing the top window with x, it will run the function to_settings.
        # same as when the button back to settings is clicked.
        # protocol() --- Registers a callback function for the given protocol. 
        # The name argument is typically one of “WM_DELETE_WINDOW” (the window is about to be deleted)
        self.top.protocol("WM_DELETE_WINDOW", self.to_settings)

        # Setting of the widgets:
        self.message_label4 = StringVar()
        
        label1 = Label(self.top, text='Tic-tac-toe',font='Helvetic 16 bold italic')
        back_button = Button(self.top, text="Back to settings",
                padx=5, pady=5, command=self.to_settings)
        label2 = Label(self.top, text=f"{self.players[0]} vs. {self.players[1]}",
                fg = '#1b1c5e', font='Helvetic 12',
                borderwidth=2, relief="groove", padx= 5, pady=5)
        label3 = Label(self.top, text="Let's Play")
        label4 = Label(self.top, textvariable=self.message_label4, font='TkDefaultFont 10')
        self.message_label4.set(f"it's your turn {self.player_x}")
        
        # Game frame
        Game_frame = Frame(self.top)
       
        self.game_btns = []
        for i in range(9):
            game_btn = Button(Game_frame, text=" ",
                            command=partial(self.click_number, i),
                            font=('Helvetica', 20), width=3)
            game_btn.grid(row=i//3, column=i%3)
            self.game_btns.append(game_btn)
        
        self.orig_color = game_btn.cget("background")
        # orig_color is SystemButtonFace

        #Play again button
        play_again_btn = Button(self.top, text="Play again",
                         padx= 5, pady=5, command=self.play_again)
        
        #layout
        label1.grid(row=0, column=0, columnspan=2, padx=80, pady=(10,0))
        label2.grid(row=1, column=0, columnspan=2, padx=80)
        label3.grid(row=2, column=0, columnspan=2, padx=80)
        label4.grid(row=3, column=0, columnspan=2, padx=80)
        Game_frame.grid(row=4, column=0, columnspan=2, padx=80)
        play_again_btn.grid(row=5, column=0, padx= 5, pady=(5,0), sticky=E)
        back_button.grid(row=5, column=1, padx=5, pady=(5,0), sticky=W)

        # Deals with computer turn if the computer player has the first turn,
        # because the computer wont trigger the function click_number
        if self.player_x == "computer":
            self.computer_1turn()
        
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

    def play_again(self):
        ''' Gets the game started. It resets all values stored during the last game,
        defines which player plays first, if the computer player goes first, 
        it deals with his first move '''
        # turn counter is reset to cero
        self.count_turns = 0

        # sets are reset to empty
        self.disable_numbers_x = set()
        self.disable_numbers_o = set()

        # buttons of the board games are reset, so that they are available to the
        # players, with no text and in their original color
        for i in range(9):
            if self.game_btns[i]['state'] == 'disabled':
                self.game_btns[i].config(state="normal", text=" ", bg=self.orig_color)
        # choose randomly the player that starts
        # applies for 1 player and 2 player choice
        random.shuffle(self.players)
        # player_x will always have the first turn!
        self.player_x = self.players[0]
        self.player_o = self.players[1] 

        self.message_label4.set(f"it's your turn {self.player_x}")

        # Deals with computer turn if the computer player has the first turn,
        # because the computer wont trigger the function click_number
        if self.player_x == "computer":
            self.computer_1turn()
        

    def click_number(self, i):
        '''It is trigger by pressing a button on the game board. 
        It places an X or an O over the pressed button and disable this 
        button, calls after the move function. 

        Parameter:
        i(int): is the number referening the position of the button in the game board
        '''
        # Human turn activated with a click in the board
        # if the other player is the computer, he plays afterwards
        if self.count_turns % 2 == 0:
            current_player = self.player_x 
            self.game_btns[i].config(state="disabled", text='X')         
            next_player = self.player_o
            self.disable_numbers_x.add(i)
            check_disable = self.disable_numbers_x
            comp_symbol = "o"
        else:
            current_player = self.player_o
            self.game_btns[i].config(state="disabled", text='O')
            next_player = self.player_x
            self.disable_numbers_o.add(i)
            check_disable = self.disable_numbers_o
            comp_symbol = "x"

        # counts human turns
        self.count_turns += 1
        self.after_move(check_disable, current_player, next_player, comp_symbol)
           

    def after_move (self, check_disable, current_player, next_player, comp_symbol=None):
        ''' Checks if there is a winner using the function player_won() or 
        if there is no more possible moves. Once a player has won, it dissables
        all the buttons on the board game. It changes the label to display who's next,
        if somebody has won or if the result is a tie '''

        if self.player_won(check_disable, "playing"):
            self.message_label4.set(f"{current_player} won!! :) ")

            # this code disable left over buttons after winning
            for i in range(9):
                if self.game_btns[i]['state'] == 'normal':
                    self.game_btns[i].config(state="disabled", text=" ")

        elif self.count_turns == 9:
             self.message_label4.set(f"It is a tie")
        else:
             self.message_label4.set(f"Your turn {next_player}")
             # handles computer turn   
             if next_player == "computer":
                 self.computer_turn(comp_symbol)
        
    def player_won(self, check_disable, game_state="trying"):
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
                if game_state == 'playing':
                    for elem in win_set:
                        self.game_btns[elem]['bg'] = '#CCFFFF'
                    return True
                elif game_state == 'trying':
                    return True
        return False
    
    def computer_1turn(self):
        # first turn is always X
        # chooses move:
        corners_center= [0,2,6,8,4]
        move = random.choice(corners_center)
        # marks the move, disables the button:
        self.game_btns[move].config(state="disabled", text='X')
        # counts a turn: 
        self.count_turns += 1
        # adds move to set of moves
        self.disable_numbers_x.add(move)
        check_disable = self.disable_numbers_x
        # defines current and next player
        current_player = self.player_x
        next_player = self.player_o
        self.after_move(check_disable, current_player, next_player)

    def computer_turn(self, comp_symbol):
        '''This function handles the computer turn '''
        # chooses move:
        move = self.deciding_computer_move(comp_symbol)
        
        # counts computer turn: 
        self.count_turns += 1      
        if comp_symbol == "x":
            # marks the move, disables the button:
            self.game_btns[move].config(state="disabled", text="X")
            # adds move to set of moves
            self.disable_numbers_x.add(move)
            check_disable = self.disable_numbers_x
            # defines current and next player
            current_player = self.player_x
            next_player = self.player_o
            print(move, check_disable)
        else: 
            self.game_btns[move].config(state="disabled", text="O")
            # adds move to set of moves
            self.disable_numbers_o.add(move)
            check_disable = self.disable_numbers_o
            # defines current and next player
            current_player = self.player_o
            next_player = self.player_x
        
        self.after_move(check_disable, current_player, next_player)

    def deciding_computer_move(self, comp_symbol):
        '''In this function the computer decides the next move
        Parameters:
        disable_numbers_o_copy(set): copy of the moves up to this moment of the computer
        disable_numbers_x_copy(set): copy of the moves up to this moment of the player
        Return
        move(int): position on the board'''
        disable_numbers_o_copy = self.disable_numbers_o.copy()
        disable_numbers_x_copy = self.disable_numbers_x.copy()

        available_moves = []
        for i in range(9):
            if self.game_btns[i]['state'] == 'normal':
                available_moves.append(i)
        # print(f'available moves for the computer {available_moves}')
        
        # identify computer player and move done by him 
        # and by its opponent
        if comp_symbol == "x":
            computer_set = disable_numbers_x_copy
            oponent_set = disable_numbers_o_copy
        else:
            computer_set = disable_numbers_o_copy
            oponent_set = disable_numbers_x_copy

        # Check for every available move if computer can win with the next move
        # if it can win self.move has a value
        for i in available_moves:
            computer_set.add(i)
            if self.player_won(computer_set):
                move = i
                return move
            computer_set.remove(i)
        # print('computer does not have a chance to win')

        # Check for every available move if the human can win with the next move
        # if the human could win next round - the computer will block him/her
        for i in available_moves:
            oponent_set.add(i)
            if self.player_won(oponent_set):
                move = i
                return move
            oponent_set.remove(i)
        # print('oponent has no chance to win')

        # Check if any of the corners and center are available to make a move
        # Center and corners are python-positions [0,2,6,8,4] in the board
        corners_center_available = []
        for i in available_moves:
            if i in [0, 2, 4, 6, 8]:
                corners_center_available.append(i)
        move = random.choice(corners_center_available)
        
        if move:
            return move
        # print('no corners available')

        # Check if any of the sides are available to make a move
        # Center and corners are python positions [1,3,5,7] in the board
        sides_available = []
        for i in available_moves:
            if i in [1, 3, 5, 7]:
                sides_available.append(i)
        move = random.choice(sides_available)

        if move:
            return move
        # print('sides only available')

# if __name__ == "__main__": 