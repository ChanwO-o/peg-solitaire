'''
Created on Oct 28, 2018

@author: cmins

Check the state of the game whether the game has finished or keep playing.
Verify the input and move.

'''


class PSGameState:
    def __init__(self, board: [[int]]):
        self.board = psBoard()

    def calcPegMiddle(self, fromRow: int, fromCol: int, toRow: int, toCol: int) -> (row, col):
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
        if isValidMove() == True:
            self.board.addPeg(toRow, toCol)
            self.boead.removePeg(fromRow, fromCol)

    def start():
        while(isFinished() != True):

            # Return false if move is not valid, return true if the move is possible.
            # 1. Check Peg if Peg exists on from coordinate
            # 2. CHen if Peg exist on to coordinate, if exist return false.
            # 3. Check if moving is digonal
            # 4. Check if Peg exists on middle of from coordinate and to coordinate
            #
    def isValidMove(fromRow: int, fromCol: int, toRow: int, toCol: int) -> bool:
        middle = calcPegMiddle(fronRow, fromCol, toRow, toCol)
        try:
            if self.board.get(fromRow, fromCol) == 0 or self.board.get(toRow, fromCol) == 1 or self.board.get(middle[0], middle[1]) == 0 or isDiagonal(fromRow, fromCol, toRow, toCol) == False:
                return False
            return True
        except:
            print("Invalid Move\n")

    def isOutOfBounds(row: int, col: int) -> bool:
        ''' Checks if location is in board '''
        if row < 0 or row > self.getRows():
            return True
        if col < 0 or col > self.getCols():
            return True
        # TODO: check for corners

    # 1. Loop all pegs and check whether there are valid moves or not
    # Return True is game state is finished.
    # Return False if game state is not finished.
    def isFinished() -> bool:
        rows = self.board.getRows()
        cols = self.board.getCols()
        for row in range(rows):
            for col in range(cols):
                peg = get(row, col)
                if peg == -1:
                    pass
                elif peg == 1:
                    moves = getPossibleMoves(row, col)
                    for i in range(len(moves)):
                        if isValidMove(row, col, moves[i][0], moves[i][1]) == True:
                            return False
        return True

    # helper function for isFinished.
    # Take row and col of current position and return all the possible moves in list.
    def getPossibleMoves(row, col) -> list of sets:
        return [(row - 2, col), (row + 2, col), (row, col - 2), (row, col + 2)]

    def isDiagonal(fromcol: int, fromrow: int, tocol: int, torow: int) -> bool:
        if (fromcol - tocol) != 0 and (fromrow - torow) != 0:
            raise PSInvalidMoveException()
        return True
