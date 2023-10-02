import random
#there are 7 functions in total

# starting statement
print("This is a TICTACTOE game with USER('X') vs. CPU('O')")
print("...have fun!\n")

#establishes user, cpu, & number of turns (for now)
player = "X"
cpu = "O"
turns = 0

# creates game board 
board = [
    ["-", "-", "-"], 
    ["-", "-", "-"], 
    ["-", "-", "-"]
]

# defines coordinates
coords = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}

# prints the gameboard
    # side note: "f" provides a way to embed expressions inside string literals, using a minimal syntax
def print_gameBoard(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end = "")
        print()
    
# checks if user input is in bounds
def in_bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("number is out of bounds!")
        return False
    else: 
        return True

# makes sure position entered is not already taken
def check_taken(user_input, coords, board):
    row, col = coords[user_input]
    if board[row][col] != "-":
        print("position is occupied.")
        return True
    return False

#player makes move 
def playerMove(user_input, board):
    row, col = coords[user_input]
    board[row][col] = player

# CPU makes a move 
def cpuMove(board):
    while True:
        cpuPos = random.randint(1,9)
        row, col = coords[cpuPos]
        if board[row][col] == "-":
            board[row][col] = cpu
            break
        
# defines winner
def winner(board, player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
    
# function that puts the whole game in play 
def gamePlay():
    global turns
    print_gameBoard(board)
    while turns < 9:
        user_input = int(input("enter placement (1-9): "))
        if not in_bounds(user_input):
            print("try re-entering")
            continue
        if check_taken(user_input, coords, board):
            print("try re-entering")
            continue
        
        playerMove(user_input, board)
        turns += 1
        if winner(board, "X"):
            print_gameBoard(board)
            print("congrats! you beat the CPU :) ")
            break
        elif turns == 9:
            print("you tied w/ the CPU...")
            break
        
        cpuMove(board)
        turns += 1
        print_gameBoard(board)
        if winner(board, "O"):
            print("tough luck! the CPU beat you :( ")
            break
        elif turns == 9:
            print_gameBoard(board)
            print("you tied w/ the CPU...")
            break
        
# main starts here 
gamePlay()
