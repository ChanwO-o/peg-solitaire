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
    def __init__(self, rows:int, cols:int):
        self.board = self.createNewBoard(rows, cols)
    
    def createNewBoard(self, rows:int, cols:int) -> [[bool]]:
        '''Creates a new game board with specified rows and columns'''
        
        
           
    def updateBoard():
        pass

    def isFinished():
        pass
    
    def isValidMove(fromrow:int, fromcol:int, torow:int, tocol:int) -> bool:
        pass

def isOutOfBounds():
    pass
