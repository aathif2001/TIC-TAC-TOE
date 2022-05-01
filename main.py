board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# ------- Global Variables -------------

# To run a While Loop
Still_not_over = True

# To change Characters for players
Start_char = 'X'

# not to show game over when someone wins the match with completing the whole board
game_over = True


# Displaying the Board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# inserting a character
def insert_character():
    global Still_not_over
    global Start_char
    # list to make sure the character a player inserts is in the range 1 - 9
    key_places = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    input_number = input('Insert the number to place your key, To Quit The Game Press uppercase E-> ')
    # to exit the game while playing
    if input_number == 'E':
        Still_not_over = False
    elif input_number in key_places:
        if board[int(input_number) - 1] == '-':
            board[int(input_number) - 1] = Start_char
            display_board()
        else:
            print('Wrong Position Choosen. Insert a valid number')
            insert_character()
    else:
        print('Wrong input. Insert a valid number')
        insert_character()


# to check if the game is over by completing the board
def check_game_over():
    global game_over
    global Still_not_over
    # if the both conditions are fullfilled only the game_over will be printed
    # here we had a conflict when someone wins the game by completing the whole board it is possible to show game over also
    if (('-' not in board) and (game_over == True)):
        Still_not_over = False
        print('Game Over')


# to change 'X' and 'O'
def change_character():
    global Start_char
    if Start_char == 'X':
        Start_char = 'O'
    elif Start_char == 'O':
        Start_char = 'X'


# checking for winning is divided into 3 Stages by checking Rows, Columns and Diagonals
def check_for_win():
    global game_over
    global Still_not_over
    column_win()
    row_win()
    diagonal_win()
    # the if statement below is used to not to show game over when someone wins the game by completing the board
    # if someone wins 'Still_not_over' will be false
    if Still_not_over == False:
        game_over = False


# checking if someone is winning through columns
def column_win():
    global Still_not_over
    if board[0] == board[3] == board[6]:
        if board[0] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False
    elif board[1] == board[4] == board[7]:
        if board[1] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False
    elif board[2] == board[5] == board[8]:
        if board[2] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False


# checking if someone is winning through rows
def row_win():
    global Still_not_over
    if board[0] == board[1] == board[2]:
        if board[0] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False
    elif board[3] == board[4] == board[5]:
        if board[3] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False
    elif board[6] == board[7] == board[8]:
        if board[6] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False


# checking if someone is winning through diagonal
def diagonal_win():
    global Still_not_over
    if board[0] == board[4] == board[8]:
        if board[0] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False
    elif board[2] == board[4] == board[6]:
        if board[2] == Start_char:
            print(Start_char + ' Won the game')
            Still_not_over = False


# To play once more
def play_again():
    global Still_not_over
    global board
    once_more = input('To Play Again press Uppercase "Y". Press any other key to end the game => ')
    if once_more == 'Y':
        Still_not_over = True
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        play_game()

# to play the game with all functions
def play_game():
    display_board()
    while Still_not_over:
        insert_character()
        check_for_win()
        check_game_over()
        change_character()
    play_again()

# at last lets play
play_game()
