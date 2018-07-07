'''
Battleship
by Eric Sheridan
20180703
'''
from random import randint
print("Welcome to Battleship!")
print("Board is squared of input.")
size = input("what size board do you want?: ")
size = int(size)
board = []
guesses = 5

for line in range(0, size):
    board.append(["O"] * size)

def print_board(board_in):
    for row in range(len(board_in)):
        print(" ".join(board_in[row]))

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in) -1)

ship_row = random_row(board)
ship_col = random_col(board)
ship_row = (ship_row - 1)
ship_col = (ship_col - 1)
### testing
print(ship_row)
print(ship_col)
### end testing
### start turn
for turn in range(guesses):
    turn = turn + 1
    print("Curent turn is %s out of %s" % (turn, guesses))
    print_board(board)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    #Result human readability
    guess_row = (guess_row - 1)
    guess_col = (guess_col - 1)

    if (guess_row == ship_row) and (guess_col == ship_col):
        print("Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = "W"
        print("Ship location: W")
        print_board(board)
    else:
        if (guess_row not in range(size)) or (guess_col not in range(size)):
            print("Thats not even on the BOARD!!")
        elif (board[guess_row][guess_col] == "X"):
                print("You already guessed Row:%s Col:%s" % (guess_row, guess_col))
        else:
            print("Sorry you missed the battleship!")
            board[guess_row][guess_col] = "X"
board[guess_row][guess_col] = "X"
board[ship_row][ship_col] = "S"
print("User guess: X  |  Ship location: S")
print_board(board)
