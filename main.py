board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# ------- Global Variables -------------

# To run a While Loop
Still_not_over = True

# To change Characters for players
Start_char = 'X'


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# display_board()

def insert_character():
    global Still_not_over
    global Start_char
    key_places = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    input_number = input('Insert the number to place your key -> ')
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


def check_game_over():
    global Still_not_over
    if '-' not in board:
        Still_not_over = False
        print('Game Over')


def change_character():
    global Start_char
    if Start_char == 'X':
        Start_char = 'O'
    elif Start_char == 'O':
        Start_char = 'X'


def check_for_win():
    global Still_not_over
    column_win()
    row_win()
    diagonal_win()


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


def play_again():
    global Still_not_over
    global board
    once_more = input('To Play Again press Uppercase "Y". Press any other key to end the game => ')
    if once_more == 'Y':
        Still_not_over = True
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        play_game()


def play_game():
    display_board()
    while Still_not_over:
        insert_character()
        check_for_win()
        check_game_over()
        change_character()
    play_again()


play_game()
