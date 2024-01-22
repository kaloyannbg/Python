#Exercise 12.6 Write a Tic-Tac-Toe program that allows two people to play the game
#against each other. In turn, ask each player which row and column they want to play. Make
#sure that the program checks if that row/column combination is empty. When a player has
#won, end the game. When the whole board is full and there is no winner, announce a draw.
#This is a fairly long program to write (60 lines or so). It will definitely help to use some
#functions. I recommend that you create a function display_board() that gets the board
#as parameter and displays it, a function getRowCol() that asks for a row or a column (depending on a parameter) and checks whether the user entered a legal value, and a function
#winner() that gets the board as argument and checks if there is a winner. Keep track of
#who the current player is using a global variable player that you can pass to a function as
#an argument if the function needs it. I also use a function opponent(), that takes the player
#as argument and returns the opponent. I use that to switch players after each move.

def display_board(board) :
    for row in range(len(board)) :
        print(row+1,' : ', end="")
        for col in range(len(board[row])) :
            print('[' + board[row][col] + ']', end="")
        print('')

def getRowCol(currBoard, player, row=0, col=0) :

    if row < 1 or row > 3 :
        return 1
    elif col < 1 or col > 3 :
        return 2
    elif currBoard[row-1][col-1] == 'x' or currBoard[row-1][col-1] == '0' :
        return 3
    else :
        currBoard[row-1][col-1] = player
        return 0

def opponent(currPlayer) :
    if(currPlayer == 'x') :
        return '0'
    return 'x'

def winner(myBoard, currPlayer) :

    if (myBoard[0][0] == currPlayer
        and myBoard[0][1] == currPlayer
        and myBoard[0][2] == currPlayer) :
        return currPlayer
    elif (myBoard[1][0] == currPlayer
        and myBoard[1][1] == currPlayer
        and myBoard[1][2] == currPlayer) :
        return currPlayer
    elif (myBoard[2][0] == currPlayer
        and myBoard[2][1] == currPlayer
        and myBoard[2][2] == currPlayer) :
        return currPlayer

    if (myBoard[0][0] == currPlayer
          and myBoard[1][1] == currPlayer
          and myBoard[2][2] == currPlayer):
        return currPlayer
    elif (myBoard[0][2] == currPlayer
          and myBoard[1][1] == currPlayer
          and myBoard[2][0] == currPlayer):
        return currPlayer

    if (        myBoard[0][0] == currPlayer
            and myBoard[1][0] == currPlayer
            and myBoard[2][0] == currPlayer):
        return currPlayer
    elif     (myBoard[0][1] == currPlayer
          and myBoard[1][1] == currPlayer
          and myBoard[2][1] == currPlayer):
        return currPlayer
    elif (    myBoard[0][2] == currPlayer
          and myBoard[1][2] == currPlayer
          and myBoard[2][2] == currPlayer):
        return currPlayer

    for row in range(len(myBoard)) :
        for col in range(len(myBoard[row])) :
            if myBoard[row][col] != 'x' and myBoard[row][col] != '0':
                return 'playednow'

    return 'no' #nowinner

board = [
            ['1' , '2' , '3'],
            ['4' , '5' , '6'],
            ['7' , '8' , '9']
        ]

currPlayer = '0'
isWinner = 'playednow'
while True :
    display_board(board)
    print("Current Player: " + currPlayer)
    rowChoice = int(input('Please choose row [1-3]: '))
    colChoice = int(input('Please choose col [1-3]: '))
    if getRowCol(board, currPlayer, rowChoice, colChoice) == 0:
        print('Success!')
        isWinner = winner(board, currPlayer)
        if(isWinner == currPlayer or isWinner == 'no') :
            print('Winner : ' + isWinner)
            break
        currPlayer = opponent(currPlayer)
    elif getRowCol(board, currPlayer, rowChoice, colChoice) == 1 :
        print('Wrong choice, row can be from [1-3]')
    elif getRowCol(board, currPlayer, rowChoice, colChoice) == 2:
        print('Wrong choice, col can be from [1-3]')
    elif getRowCol(board, currPlayer, rowChoice, colChoice) == 3:
        print('Already choosed.')
