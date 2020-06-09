# Tic Tac Toe


def create_a_blank_board():
    '''This function returns a empty list of 3 of list with 3 position
    [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    '''
    list_of_three = []
    for i in range(3):
        list_of_three.append([])
        for j in range(3):
            list_of_three[i].append(' ')
    return list_of_three


def display_board(board):
    '''This function takes a list of list representing the values of the board 
    and displays them as a tic tac toe human friendly board by printing it'''
    line_counter = 0
    print('\n')
    for i, line in enumerate(board):
        print(' '+' | '.join(line))
        if i < 2:
            print('---+---+---')
        line_counter += 1


def position_indicator_initial():
    '''This function uses the create_a_blank_board and returns the initial 
    position map as a list of list, so that the user knows how to select a 
    position in the board'''
    board = create_a_blank_board()
    position = 1
    for i in range(3):
        for j in range(3):
            board[i][j] = str(position)
            position += 1
    return board


# This function doesn't have a return because it is passed as a reference
# it will be then modified anyways, the same happens with register_move()
# function bellow
def register_position_move(position_map, move):
    '''This function updates the list of list position map, with the move of a 
    player, so that the user knows which positions are still selectable on the 
    board'''
    move = int(move)-1
    i = int(move) // 3
    j = int(move) % 3
    position_map[i][j] = ' '


def register_move(board, move, current_player):
    '''This function updates the game board, adding the move of a player'''
    move = int(move)-1
    i = int(move) // 3
    j = int(move) % 3
    if current_player == players[0]:
        board[i][j] = 'X'
    else:
        board[i][j] = 'O'


def check_input(move, position_map):
    ''' This funcion checks if the move given by the player is valid, if it is a 
    valid number between 0-9 and if the number is available in the position map, 
    and if he input is a number, it returns true for valid or false for invalid '''
    try:
        int(move)
    except:
        return False

    if 0 < int(move) < 10:
        i = (int(move)-1) // 3
        if move in position_map[i]:
            return True
    return False


def check_if_player_won(board, current_player):
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
    '''This function takes the list of players and the current player and 
    change the current_player, so both players switch in each turn'''
    if current_player == players[0]:
        current_player = players[1]
    else:
        current_player = players[0]
    return current_player


print('Lets play Tic-Tac-Toe')
# initial board
board = create_a_blank_board()
display_board(board)


print('\n'+'Make your move by chossing a number on this board')
# Board indicating initially available positions of the board

# To make a second board to trace position, I have to create a second blank!
position_map = position_indicator_initial()
display_board(position_map)

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
        if check_input(move_player, position_map) == True:
            move = 'accepted'

    # insert a X or  O in the position
    register_move(board, move_player, current_player)
    display_board(board)

    # update position map, with available positions
    register_position_move(position_map, move_player)
    display_board(position_map)
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
