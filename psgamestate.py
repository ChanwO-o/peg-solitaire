'''
Created on Oct 28, 2018

@author: cmins
'''

class PSOutOfBoundsException(Exception):
    pass

class PSInvalidMoveException(Exception):
    pass

class PSGameOverException(Exception):
    pass


class PSGameState:
    
    def __init__(self, board:[[int]]):
##        self.board = createNewBoard(rows, cols)
        pass

    def get(self, row:int, col:int) -> int:
        ''' Returns value of peg at coordinate (-1 0 or 1) '''
        pass

    def set(self, row:int, col:int, val:int) -> None:
        ''' Sets coordinate value to val '''
        pass

    def getRows(self) -> int:
        ''' Returns number of rows of board '''
        pass

    def getCols(self) -> int:
        ''' Returns number of cols of board '''
        pass
        
    def updateBoard():
        pass

    def isFinished():
        pass
    
    def isValidMove(fromrow:int, fromcol:int, torow:int, tocol:int) -> bool:
        pass

    def isOutOfBounds(row:int, col:int) -> bool:
        ''' Checks if location is in board '''
        if row < 0 or row > self.getRows():
            return True
        if col < 0 or col > self.getCols():
            return True
        ## TODO: check for corners
