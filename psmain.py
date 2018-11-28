'''
Created on Oct 28, 2018

@author: cmins
'''
import psgamestate

GAMESTATE = None
    
def getNewBoard(rows:int, cols:int) -> [[int]]:
    ''' Creates a new game board with specified rows and columns '''
    board = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(1)
        board.append(row)
    return board

def makeMove() -> None:
    ''' '''
    pass

def printBoard() -> None:
    ''' Display the board on the console '''
    pass


if __name__== "__main__":
    board = getNewBoard(10, 10)
    GAMESTATE = psgamestate.PSGameState(board)
    printBoard()
