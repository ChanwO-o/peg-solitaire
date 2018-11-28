'''
Created on Oct 28, 2018

@author: cmins

Check the state of the game whether the game has finished or keep playing.
Verify the input and move.

'''

import psboard
from psExceptions import *


class PSGameState:
    def __init__(self):
        self.board = psboard.psBoard()

    def calcPegMiddle(self, fromRow: int, fromCol: int, toRow: int, toCol: int) -> ():
        if fromRow - toRow > 0 and fromCol - toCol == 0:
            return (fromRow - 1, fromCol)
        elif fromRow - toRow < 0 and fromCol - toCol == 0:
            return (fromRow + 1, fromCol)
        elif fromCol - toCol > 0 and fromRow - toRow == 0:
            return (fromRow, fromCol - 1)
        elif fromCol - toCol < 0 and fromRow - toRow == 0:
            return (fromRow, fromCol + 1)
        else:
            pass  # throwexcemption

    def makeMove(self, fromRow: int, fromCol: int, toRow: int, toCol: int) -> None:
        ''' add and remove peg on the board '''
        if self.isValidMove() == True:
            self.board.addPeg(toRow, toCol)
            self.boead.removePeg(fromRow, fromCol)

<<<<<<< HEAD
    def start(self):
=======
>>>>>>> e6845a3e7bbd785bf27a8a00ea14a5be8b7fb1a0
        while True:
            try:
                self.isFinished()

                while True:
                    from_input = getFromInput()
                    to_input = getToInput()
                    try:
                        self.makeMove(from_move[0], from_move[1], to_move[0], to_move[1])
                        break

                    except (PSInvalidMoveException()):
                        print("INVALID MOVE")

            except (PSGameOverException):
                print("The Game is Over!")
                break

    # Return false if move is not valid, return true if the move is possible.
    # 1. Check Peg if Peg exists on from coordinate
    # 2. CHen if Peg exist on to coordinate, if exist return false.
    # 3. Check if moving is digonal
    # 4. Check if Peg exists on middle of from coordinate and to coordinate
    #

    def isValidMove(self, fromRow: int, fromCol: int, toRow: int, toCol: int) -> bool:
        middle = self.calcPegMiddle(fromRow, fromCol, toRow, toCol)
        try:
            if self.board.get(fromRow, fromCol) == 0 or self.board.get(toRow, fromCol) == 1 or self.board.get(middle[0], middle[1]) == 0 or self.isDiagonal(fromRow, fromCol, toRow, toCol) == False:
                return False
            return True
        except (PSOutOfBoundsException):
            return False

    # 1. Loop all pegs and check whether there are valid moves or not
    # Return True is game state is finished.
    # Return False if game state is not finished.
    def isFinished(self) -> bool:
        rows = self.board.getRows()
        cols = self.board.getCols()
        for row in range(rows):
            for col in range(cols):
                try:
                    peg = self.board.get(row, col)
                except:
                    break
                if peg == -1:
                    pass
                elif peg == 1:
                    moves = self.getPossibleMoves(row, col)
                    for i in range(len(moves)):
                        if self.isValidMove(row, col, moves[i][0], moves[i][1]) == True:
                            return False
        raise PSGameOverException()

    # helper function for isFinished.
    # Take row and col of current position and return all the possible moves in list.
    def getPossibleMoves(self, row, col) -> list:
        return [(row - 2, col), (row + 2, col), (row, col - 2), (row, col + 2)]

    def isDiagonal(self, fromcol: int, fromrow: int, tocol: int, torow: int) -> bool:
        if (fromcol - tocol) != 0 and (fromrow - torow) != 0:
            raise PSInvalidMoveException()
        return True


def getFromInput() -> (int, int):
    while True:
        from_input = input("FROM: ")
        from_input = from_input.split()
        if len(from_input) == 2:
            try:
                from_row = int(from_input[0])
                from_col = int(from_input[1])
                from_move = (from_row, from_col)
                break
            except:
                print("INVALID MOVE")
        else:
            print("INVALID MOVE")


def getToInput() -> (int, int):
    while True:
        to_input = input("TO: ")
        to_input = to_input.split()
        if len(to_input) == 2:
            try:
                to_row = int(to_input[0])
                to_col = int(to_input[1])
                to_move = (to_row, to_col)
                break
            except:
                print("INVALID MOVE")
        else:
            print("INVALID MOVE")
