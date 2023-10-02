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

"""
*** list, 2x function call w/ parameter, iteration

1. List: board
board = [
    ["-", "-", "-"], 
    ["-", "-", "-"], 
    ["-", "-", "-"]
]
The list in this program is the 3x3 nested list that is the board. It is beneficial to make it a list rather 
than a tuple because throughout the game, the components of this list ("-") will be changed to either X or O when 
the game is being played. The whole purpose of this list is to serve as the board. 

2. Two function calls w/ parameters: playerMove & cpuMove
** both functions are called in gamePlay function
def playerMove(user_input, board):
    row, col = coords[user_input]
    board[row][col] = user
The first function with parameters is playerMove which takes the parameters of user input and the board to make the 
player's move. This function passes on the integer between 1-9 that the user enters and converts it into coordinates 
on the board. Earlier on, we established user = "X" so when we make this equal to user, the "-" on the board will 
now change into an "X".
def cpuMove(board):
    while True:
        cpuPos = random.randint(1,9)
        row, col = coords[cpuPos]
        if board[row][col] == "-":
            board[row][col] = cpu
            Break
The second function with parameters is cpuMove which generates a random number, converts into a coordinate on the 
board, and implements an "O". This function takes in the parameter of the board and the reason it starts with a loop 
is because it repeats the step inside until the position isn't filled. After it does, it breaks out of the loop. 

3. Iteration: gamePlay (while loop)
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
         print("you tied w/ the CPU...")
         break
This is the gamePlay function which is a big while loop that iterates a maximum of 9 turns and calls all previous 
functions for the game to run. Each time someone goes, a turn is added so in the end if all turns are used up, it 
prints out the tie statement. With each iteration, we ask for user input and check to see if the number is between 
1-9 and if that place is taken on the board. If so, those functions get the player to try again. If you type an 
integer that meets requirements, it will place "X" onto the corresponding position on the board. After your go, 
it will check for winners and draws. Next the CPU makes its turn randomly and prints the gameboard. After checking 
for winners and lower, the loop will go again until someone wins or both tie. 
"""