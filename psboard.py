'''
Created on Oct 28, 2018

@author: cmins
'''


class psBoard:
    def __init__(self):
        self._board = getNewBoard(7, 7)

    def getNewBoard(rows: int, cols: int) -> [[int]]:
        ''' Creates a new game board with specified rows and columns '''
        board = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(1)   # fill with 1
            board.append(row)

        board[int(rows/2)][int(cols/2)] = 0 # center empty
        return board

    def getBoard(self) -> [[int]]:
        ''' Returns the board '''
        return self._board

    def get(self, row: int, col: int) -> int:
        ''' Returns value of peg at coordinate (-1 0 or 1) '''
        # TODO check if coordinate is not outofbounds
        return self._board[row][col]

    def addPeg():
        pass

    def removePeg():
        pass
    
    def getRows(self) -> int:
        ''' Returns number of rows of board '''
        return len(self._board)

    def getCols(self) -> int:
        ''' Returns number of cols of board '''
        return len(self._board[0])



    def printBoard() -> None:
        ''' Display the board on the console '''
        pass
