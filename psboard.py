'''
Created on Oct 28, 2018

@author: cmins
'''
# Every coordinates of first value is rows and second value is col

import psexceptions
import psgamestate


class PSBoard:
    def __init__(self):
        self._board = self.getNewBoard(7, 7)
        # Joowon Jan,04,2019
        # Add variable to store the value of number of rows and columns
        # Set dafault as 7
        # Will be used later when we add resizing of board.
        self.numOfCols = 7
        self.numOfRows = 7
        # end

    def getNewBoard(self, rows: int, cols: int) -> [[int]]:
        ''' Creates a new game board with specified rows and columns '''
        board = []
        boundindex = (rows - 3) / 2
        for r in range(rows):
            row = []
            for c in range(cols):
                if r < boundindex or r > (rows - boundindex - 1):
                    if c < boundindex or c > (cols - boundindex - 1):
                        row.append(-1)
                        continue
                row.append(1)   # fill with 1
            board.append(row)

        board[int(rows/2)][int(cols/2)] = 0  # center empty
        return board

    def getBoard(self) -> [[int]]:
        ''' Returns the board '''
        return self._board

    def get(self, row: int, col: int) -> int:
        ''' Returns value of peg at coordinate (-1 0 or 1) '''
        if self.isOutOfBounds(row, col):
            raise psexceptions.PSOutOfBoundsException()
        return self._board[row][col]

    def addPeg(self, row: int, col: int) -> None:
        self._board[row][col] = 1

    def removePeg(self, row: int, col: int) -> None:
        self._board[row][col] = 0

    def getRows(self) -> int:
        ''' Returns number of rows of board '''
        # return len(self._board)
        # Joowon Jan,04,2019
        # This should return exact value of length
        # I changed it to return variable
        return self.numOfRows
        # end

    def getCols(self) -> int:
        ''' Returns number of cols of board '''
        # return len(self._board[0])
        # Joowon Jan,04,2019
        # return len(self._board)
        # This should return exact value of length
        # I changed it to return variable
        return self.numOfCols
        # end

	# Chan Woo, Jan, 23 moved coordinate calculation functions from psgamestate to psboard
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
			
    def isDiagonal(self, fromcol: int, fromrow: int, tocol: int, torow: int) -> bool:
        if (fromcol - tocol) != 0 and (fromrow - torow) != 0:
            return False
        return True
		
    def isOutOfBounds(self, row: int, col: int) -> bool:
        ''' Checks if location is in board '''
        if row < 0 or row > self.getRows():
            return True
        if col < 0 or col > self.getCols():
            return True
        # TODO: check for corners

    def printBoard(self) -> None:
        ''' Display the board on the console '''
        for r in range(self.getRows()):
            for c in range(self.getCols()):
                if self.get(r,c) == -1:
                    print('x', end=' ')
                else:
                    print(self.get(r, c), end=' ')
            print('\n')