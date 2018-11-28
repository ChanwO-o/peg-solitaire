    def isValidMove(fromrow: int, fromcol: int, torow: int, tocol: int) -> bool:
        pass

    def isOutOfBounds(row: int, col: int) -> bool:
        ''' Checks if location is in board '''
        if row < 0 or row > self.getRows():
            return True
        if col < 0 or col > self.getCols():
            return True
        # TODO: check for corners
