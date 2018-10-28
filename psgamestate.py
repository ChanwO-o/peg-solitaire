'''
Created on Oct 28, 2018

@author: cmins
'''

class PSOutOfBoundsException(Exception):
    pass

class PSInvalidMove(Exception):
    pass

class PSGameOverError(Exception):
    pass

class PSGameState:
    def __init__(self, rows:int, cols:int):
        self.board = psboard()


def updateBoard():
    pass

def isFinished():
    pass

def isValidMove(fromrow:int, fromcol:int, torow:int, tocol:int) -> bool:
    pass

def isOutOfBounds():
    pass