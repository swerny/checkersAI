
import random
from itertools import product
from copy import deepcopy, error

def play(agents):
    board = [
        ['X',' ','X',' ','X',' ','X',' '],
        [' ','X',' ','X',' ','X',' ','X'],
        ['X',' ','X',' ','X',' ','X',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','O',' ','O',' ','O',' ','O'],
        ['O',' ','O',' ','O',' ','O',' '],
        [' ','O',' ','O',' ','O',' ','O']
    ]

    isWinner = 0
    counter = 0
    while not isWinner:
        gamePiece = 'XO'[counter%2]
        move = agents[counter%2](board.copy(), gamePiece)
        if move != None:
            singleMove(board, move, gamePiece)
        else:
            isWinner = 1
        show(board)
        counter = counter + 1
    print("Game Over: "+gamePiece+" has no available moves")
 

def getMoves(board, gamePiece):
    validMoves = []
    for y,x in product(range(0, 8), range(0, 8)):
        if (gamePiece == 'X'):
            if (board[y][x] == 'X'):
                if y < 7 and x < 7:
                    if board[y+1][x+1] == ' ':
                        validMoves.append(([x,y],[x+1, y+1],0))
                if y < 6 and x < 6:
                    if board[y+1][x+1] == 'O' and board[y+2][x+2] == ' ':
                            validMoves.append(([x,y],[x+2, y+2],1))
                if y < 7 and x > 0:
                    if board[y+1][x-1] == ' ':
                        if not [x-1, y+1] in validMoves:
                            validMoves.append(([x,y],[x-1, y+1],0))
                if y < 6 and x > 1:
                    if board[y+1][x-1] == 'O' and board[y+2][x-2] == ' ':
                        if not [x-2, y+2] in validMoves:
                            validMoves.append(([x,y],[x-2, y+2],2))   
            if (board[y][x] == 'x'):
                if y < 7 and x < 7:
                    if board[y+1][x+1] == ' ':
                        validMoves.append(([x,y],[x+1, y+1],0))
                if y < 6 and x < 6:
                    if board[y+1][x+1].lower() == 'o' and board[y+2][x+2] == ' ':
                            validMoves.append(([x,y],[x+2, y+2],1))
                if y < 7 and x > 0:
                    if board[y+1][x-1] == ' ':
                        if not [x-1, y+1] in validMoves:
                            validMoves.append(([x,y],[x-1, y+1],0))
                if y < 6 and x > 1:
                    if board[y+1][x-1].lower() == 'o' and board[y+2][x-2] == ' ':
                        if not [x-2, y+2] in validMoves:
                            validMoves.append(([x,y],[x-2, y+2],2)) 
                if y > 0 and x < 7:
                    if board[y-1][x+1] == ' ':
                        validMoves.append(([x,y],[x+1, y-1],0))
                if y > 1 and x < 6:
                    if board[y-1][x+1].lower() == 'o' and board[y-2][x+2] == ' ':
                            validMoves.append(([x,y],[x+2, y-2],3))
                if y > 0 and x > 0:
                    if board[y-1][x-1] == ' ':
                        if not [x-1, y-1] in validMoves:
                            validMoves.append(([x,y],[x-1, y-1],0))
                if y > 1 and x > 1:
                    if board[y-1][x-1].lower() == 'o' and board[y-2][x-2] == ' ':
                        if not [x-2, y-2] in validMoves:
                            validMoves.append(([x,y],[x-2, y-2],4))       
        elif (gamePiece == 'O'):
            if (board[y][x] == 'O'):
                if y > 0 and x < 7:
                    if board[y-1][x+1] == ' ':
                        validMoves.append(([x,y],[x+1, y-1],0))
                if y > 1 and x < 6:
                    if board[y-1][x+1] == 'X' and board[y-2][x+2] == ' ':
                            validMoves.append(([x,y],[x+2, y-2],1))
                if y > 0 and x > 0:
                    if board[y-1][x-1] == ' ':
                        if not [x-1, y-1] in validMoves:
                            validMoves.append(([x,y],[x-1, y-1],0))
                if y > 1 and x > 1:
                    if board[y-1][x-1] == 'X' and board[y-2][x-2] == ' ':
                        if not [x-2, y-2] in validMoves:
                            validMoves.append(([x,y],[x-2, y-2],2))
            if (board[y][x] == 'o'):
                if y < 7 and x < 7:
                    if board[y+1][x+1] == ' ':
                        validMoves.append(([x,y],[x+1, y+1],0))
                if y < 6 and x < 6:
                    if board[y+1][x+1].lower() == 'x' and board[y+2][x+2] == ' ':
                            validMoves.append(([x,y],[x+2, y+2],3))
                if y < 7 and x > 0:
                    if board[y+1][x-1] == ' ':
                        if not [x-1, y+1] in validMoves:
                            validMoves.append(([x,y],[x-1, y+1],0))
                if y < 6 and x > 1:
                    if board[y+1][x-1].lower() == 'x' and board[y+2][x-2] == ' ':
                        if not [x-2, y+2] in validMoves:
                            validMoves.append(([x,y],[x-2, y+2],4)) 
                if y > 0 and x < 7:
                    if board[y-1][x+1] == ' ':
                        validMoves.append(([x,y],[x+1, y-1],0))
                if y > 1 and x < 6:
                    if board[y-1][x+1].lower() == 'x' and board[y-2][x+2] == ' ':
                            validMoves.append(([x,y],[x+2, y-2],1))
                if y > 0 and x > 0:
                    if board[y-1][x-1] == ' ':
                        if not [x-1, y-1] in validMoves:
                            validMoves.append(([x,y],[x-1, y-1],0))
                if y > 1 and x > 1:
                    if board[y-1][x-1].lower() == 'x' and board[y-2][x-2] == ' ':
                        if not [x-2, y-2] in validMoves:
                            validMoves.append(([x,y],[x-2, y-2],2))
    return validMoves  

def getMovesFromPos(board, x, y):
    validMoves = []
    if y > 0 and x < 7:
        if board[y-1][x+1] == ' ':
            validMoves.append(([x,y],[x+1, y-1],0))
    if y > 1 and x < 6:
        if board[y-1][x+1] == 'X' and board[y-2][x+2] == ' ':
            validMoves.append(([x,y],[x+2, y-2],1))
    if y > 0 and x > 0:
        if board[y-1][x-1] == ' ':
            if not [x-1, y-1] in validMoves:
                validMoves.append(([x,y],[x-1, y-1],0))
    if y > 1 and x > 1:
        if board[y-1][x-1] == 'X' and board[y-2][x-2] == ' ':
            if not [x-2, y-2] in validMoves:
                validMoves.append(([x,y],[x-2, y-2],2))
    return validMoves  


def randomPlayer(board, gamePiece):
    moves = getMoves(board, gamePiece)
    if len(moves) > 0:
        index = random.randint(0, len(moves)-1)
        return moves[index]
    else:
        return None

def singleMove(board, move, gamePiece):
        start = move[0]
        end = move[1]
        x = end[0]
        y = end[1]
        isUpper = board[start[1]][start[0]].isupper()
        board[start[1]][start[0]] = ' '

        if isUpper:
            board[end[1]][end[0]] = gamePiece
            if move[2] == 1 and gamePiece == 'X':
                if x > 0 and y > 0:
                    board[end[1]-1][end[0]-1] = ' '
            elif move[2] == 2 and gamePiece == 'X':
                if x < 7 and y > 0:
                    board[end[1]-1][end[0]+1] = ' '

            if move[2] == 1 and gamePiece == 'O':
                if x > 0 and y < 7:
                    board[end[1]+1][end[0]-1] = ' '
            elif move[2] == 2 and gamePiece == 'O':
                if x < 7 and y < 7:
                    board[end[1]+1][end[0]+1] = ' '
        else:
            board[end[1]][end[0]] = gamePiece.lower()
            if move[2] == 1 and gamePiece == 'X':
                if x > 0 and y > 0:
                    board[end[1]-1][end[0]-1] = ' '
            elif move[2] == 2 and gamePiece == 'X':
                if x < 7 and y > 0:
                    board[end[1]-1][end[0]+1] = ' '
            elif move[2] == 3 and gamePiece == 'X':
                if x > 0 and y < 7:
                    board[end[1]+1][end[0]-1] = ' '
            elif move[2] == 4 and gamePiece == 'X':
                if x < 7 and y < 7:
                    board[end[1]+1][end[0]+1] = ' '

            if move[2] == 1 and gamePiece == 'O':
                if x > 0 and y < 7:
                    board[end[1]+1][end[0]-1] = ' '
            elif move[2] == 2 and gamePiece == 'O':
                if x < 7 and y < 7:
                    board[end[1]+1][end[0]+1] = ' '
            elif move[2] == 3 and gamePiece == 'O':
                if x > 0 and y > 0:
                    board[end[1]-1][end[0]-1] = ' '
            elif move[2] == 4 and gamePiece == 'O':
                if x < 7 and y > 0:
                    board[end[1]-1][end[0]+1] = ' '

        if gamePiece == 'X':
            if end[1] > 6:
                board[end[1]][end[0]] = 'x'
        elif gamePiece == 'O':
            if end[1] < 1:
                board[end[1]][end[0]] = 'o'

def betterRandomPlayer(board, gamePiece):
    moves = getMoves(board, gamePiece)
    betterMoves = []
    for move in moves:
        if gamePiece == 'X':
            oppPiece = 'O'
        else:
            oppPiece = 'X'

        newBoard = deepcopy(board)
        count1 = countPieces(newBoard, oppPiece)
        count2 = 0
        singleMove(newBoard, move, gamePiece)
        count2 = countPieces(newBoard, oppPiece)
        if count2 < count1:
            betterMoves.append(move) 

    if len(betterMoves) > 0:
        index = random.randint(0, len(betterMoves)-1)
        return betterMoves[index]  
    elif len(moves) > 0:
        index = random.randint(0, len(moves)-1)
        return moves[index]
    else:
        return None

def realPlayer(board, gamePiece):
    try:
        startVal = input("What piece would you like to move?: ")
        x = int(startVal[0])
        y = int(startVal[2])
        possibleMoves = getMovesFromPos(board, x, y)
        if len(possibleMoves) == 0:
            raise ValueError
        counter = 1
        for move in possibleMoves:
            print(str(counter)+": "+str(move[1]))
            counter = counter + 1
        endVal = input("Where would you like to move?: ")
        start = [x, y]
        end = possibleMoves[int(endVal)-1][1]
        return (start, end, possibleMoves[int(endVal)-1][2])
    except ValueError: 
        print("Either invalid input or no moves possible, please try again!")
        return realPlayer(board, gamePiece)
        

def AI(board, gamePiece):
    myBoard = deepcopy(board)
    possibleMoves = []
    legalMoves = getMoves(myBoard, gamePiece)
    while len(legalMoves) > 0:
        move = legalMoves.pop()
        wins = 0
        for n in range(20):
            newBoard = deepcopy(myBoard)
            result = playThrough([AI, randomPlayer],newBoard, 0, move)
            if result == gamePiece:
                wins = wins + 1
        possibleMoves.append([move, wins])
    mostWins = 0
    bestMove= ""
    if len(possibleMoves) > 0:
        for x in possibleMoves:
            if x[1] >= mostWins:
                mostWins = x[1]
                bestMove = x[0]
        return bestMove
    else:
        return None

def playThrough(agents, board, i, firstMove):
    try:
        if len(getMoves(board, 'X')) == 0 or countPieces(board, "X") == 0:
            return 'O'
        elif len(getMoves(board, 'O')) == 0 or countPieces(board, "X") == 0:
            return 'X'
        else:
            gamePiece = 'XO'[i%2]
            if i == 0:
                move = firstMove
            else: 
                move = betterRandomPlayer(board.copy(), gamePiece)
            singleMove(board, move, gamePiece)
        return playThrough([AI, randomPlayer], board, i+1, firstMove)
    except RecursionError:
        return 'O'

        

def show(board):
    print("-0 1 2 3 4 5 6 7-")
    for y in range(0,8):
        print(f"|{' '.join(board[y])}|"+ str(y))
    print("-----------------")

def countPieces(board, gamePiece):
    xCounter = 0
    oCounter = 0
    for y,x in product(range(0, 7), range(0, 7)):
        if (gamePiece == 'X'):
            if (board[y][x] == 'X' or board[y][x] == 'x'):
                xCounter = xCounter + 1
        if (gamePiece == 'O'):
            if (board[y][x] == 'O' or board[y][x] == 'o'):
                oCounter = oCounter + 1
    if gamePiece == 'X':
        return xCounter
    else: 
        return oCounter

if __name__ == '__main__':
    myPlayer = AI
    opponent = realPlayer
    play([myPlayer, opponent])
    # board = [
    #     ['o',' ','o',' ',' ',' ',' ',' '],
    #     [' ',' ',' ',' ',' ',' ',' ',' '],
    #     [' ',' ',' ',' ',' ',' ',' ',' '],
    #     [' ',' ',' ',' ',' ',' ',' ',' '],
    #     [' ',' ',' ',' ',' ',' ',' ',' '],
    #     [' ',' ',' ',' ',' ',' ',' ',' '],
    #     [' ',' ',' ',' ',' ',' ',' ',' '],
    #     [' ',' ',' ',' ',' ',' ',' ',' ']
    # ]
    # print(getMoves(board, "O"))
    # print(betterRandomPlayer(board, "O"))
