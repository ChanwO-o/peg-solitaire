'''
Created on Oct 28, 2018

@author: cmins

Check the state of the game whether the game has finished or keep playing.
Verify the input and move.

'''


class PSGameState:

    def __init__(self, board: [[int]]):
        self.board = psBoard()

    def makeMove(self, row: int, col: int, val: int) -> None:
        ''' add and remove peg on the board '''
        self.board[row][col] = val
        self.board.add()
        self.boead.remove()

    def start():
        pass

    def isValidMove(fromRow: int, fromCol: int, toRow: int, toCol: int) -> bool:
        if()

    def isOutOfBounds(row: int, col: int) -> bool:
        ''' Checks if location is in board '''
        if row < 0 or row > self.getRows():
            return True
        if col < 0 or col > self.getCols():
            return True
        # TODO: check for corners

    def isFinished() -> bool:
        pass
