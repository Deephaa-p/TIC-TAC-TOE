import random
board = ["-","-","-","-","-","-","-","-","-"]
winner= None
gamestatus = True
currentplayer = "x"

def playboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def userinput(board):

    inp = int(input("select number from 1 to 9:"))
    if board[inp-1] == "-":
         board[inp-1] = currentplayer
    else:
        print("the place is taken already")

def horizontalwin(board):
    global winner

    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True
def diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True
def win(board):
    global gamestatus
    if horizontalwin(board):
        playboard(board)
        print(f"The winner is {winner}!")
        gamestatus = False

    elif checkRow(board):
        playboard(board)
        print(f"The winner is {winner}!")
        gamestatus = False

    elif diagonal(board):
        playboard(board)
        print(f"The winner is {winner}!")
        gamestatus = False
def tie(board):
    global gamestatus
    if "-" not in board:
        playboard(board)
        print("its tie")
        gamestatus=False

def switchplayer():
    global currentplayer
    if currentplayer == "x":

        currentplayer="o"
    else:
        currentplayer="x"
def computerturn(board):


    while currentplayer == "o":
      position = random.randint(0, 8)
      if board[position] == "-":
         board[position]="o"
         switchplayer()


while gamestatus:
 playboard(board)
 userinput(board)
 win(board)
 tie(board)
 switchplayer()
 computerturn(board)

 win(board)
 tie(board)





