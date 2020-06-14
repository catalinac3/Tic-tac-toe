# Tic Tac Toe


def create_a_blank_board():
    ''' Creates a list of 3 lists, each of them with 3 empty positions
    Returns (list): 
        [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    '''
    list_of_three = []
    for i in range(3):
        list_of_three.append([])
        for j in range(3):
            list_of_three[i].append(' ')
    return list_of_three


def display_board(board):
    ''' Takes a list of 3 list and displays it in the terminal 
    as a tic tac toe board using print()

    Parameter:
    board (list): list of 3 lists with 3 items each
    '''
    This function
    for i, line in enumerate(board):
        print(' '+' | '.join(line))
        if i < 2:
            print('---+---+---')
    print()


def position_indicator_initial():
    '''Uses the create_a_blank_board() funtion and creates the position board
    so that the user knows how to make a move, this by chossing a number between
    1 to 9 

    Returns (list): initial position board as a list of list with numbers from 
    1-9 
    '''
    board = create_a_blank_board()
    position = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = str(position)
            position += 1
    return board


def check_input(move, position_board):
    ''' Checks if the input of the player for his move is valid or invalid:
     - is it a number between 1-9 ?
     - is it a number, that is available in the position board ? 

    Parameters:
    move(int):
    position_board(list):

    Returns:
    (bool):if the input is valid the function returns True, otherwise it 
    returns False
    '''
    try:
        int(move)
    except:
        return False

    if 0 < int(move) < 10:
        i = (int(move)-1) // 3
        if move in position_board[i]:
            return True
    return False


# The following functions: register_position_move() and the register_move(),
# don't need a return value because the list of list is passed as a reference.
# It will be modified anyway, by default in python.

def register_position_move(position_board, move):
    '''Updates the list of list position board, with the move of a 
    player, by making this position empty and unavailabLe for future moves 
    during the game.

    Parameters:
    position_board (list): list of 3 lists with 3 items each
    move (int): number between 1-9
    '''
    move = int(move)-1
    i = int(move) // 3
    j = int(move) % 3
    position_board[i][j] = ' '


def register_move(board, move, current_player):
    '''Updates the game board, adding the move of a player, X for the x_player 
    and O for the o_player

    Parameters:
    board(list)
    move(int)
    current_player(str): 'player_X' or 'player O'
    '''

    move = int(move)-1
    i = int(move) // 3
    j = int(move) % 3
    if current_player == players[0]:
        board[i][j] = 'X'
    else:
        board[i][j] = 'O'


def check_if_player_won(board, current_player):
    '''Checks if the current_player won, does he has 3 in a row
    horizontally, vertically or diagonally.

    Parameters:
    current_player(str)
    board(list)

    Returns:
    (bool): True if the player has won, False if he hasn't
     '''
    if current_player == players[0]:
        sign = 'X'
    else:
        sign = 'O'
    # checking for a complete horizontal and vertical lines
    for i in range(3):
        x_hcount = 0
        x_vcount = 0
        for j in range(3):
            # for horizontal:
            if board[i][j] == sign:
                x_hcount += 1
                if x_hcount == 3:
                    return True
            # for vertical
            if board[j][i] == sign:
                x_vcount += 1
                if x_vcount == 3:
                    return True
    # checking for diagonal lines
    x_d1count = 0
    x_d2count = 0
    for i in range(3):
        # first diagonal
        if board[i][i] == sign:
            x_d1count += 1
            if x_d1count == 3:
                return True
        # second diagonal
        if board[i][2-i] == sign:
            x_d2count += 1
            if x_d2count == 3:
                return True


def change_player(players, current_player):
    '''change the current_player to the other player, it determines how's turn 
    is it

    Parameters:
    players(list): contains two string items, each one refering to a player
    current_player(str)
    '''
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]
    return current_player


print('Lets play Tic-Tac-Toe')
# initial board
board = create_a_blank_board()
display_board(board)


print('Make your move by chossing a number on this board')
# Board indicating initially available positions of the board

# To make a second board to trace position, I have to create a second blank!
position_board = position_indicator_initial()
display_board(position_board)

players = ['player X', 'player O']

player_won = False

turns = 0

current_player = players[0]

while player_won == False and turns < 9:

    # ask player for input
    # check if the input is a valid, ask again if is not!
    move = 'not accepted'
    while move == 'not accepted':
        move_player = input(
            f'\n{current_player}! Where do you want to make your next move: ')
        if check_input(move_player, position_board) == True:
            move = 'accepted'

    # insert a X or  O in the position
    register_move(board, move_player, current_player)
    display_board(board)

    # update position map, with available positions
    register_position_move(position_board, move_player)
    display_board(position_board)
    turns += 1

    # check if player has won
    if check_if_player_won(board, current_player) == True:
        player_won = True
        print('you won!!!')
        print(f'Congrats {current_player}')
        break

    # change player:
    current_player = change_player(players, current_player)


if player_won == False:
    print('sorry no more moves!')
    print('This time nobody won')
