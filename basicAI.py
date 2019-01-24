from collections import defaultdict
import psgamestate
import psboard
import math


class AI:
    state = defaultdict()
    depth = 0
    gameState = psgamestate.PSGameState()
    gameBoard = psboard.psBoard()
    # Joowon Suh, Jan, 23
    lastMove = []  # to store the last move which is going to be used to calculate the next possible moves
    currentPossibleMoves = defaultdict(list())  # to store the possible moves from current state.

    # Joowon Suh, Jan, 23
    # get coordinates of pegs which can be moved into current coordinate
    # input = cordinate of empty slot
    # output = the list of codinates of slots whose pegs can be move into input cordinate.
    def getCoordinates(r, c) -> [(int, int)]:
        return [(r-2, c), (r, c-2), (r+2, c), (r, c+2)]

    # Joowon Suh, Jan, 23
    # get all possible moves from current game state
    # If state level is 0( which means game has just started ) then only the center is empty slot
    # If state level is not 0 then use last move to calc the empty slots
    # input = None
    # outpuy = dictionary of possible moves in the form of { ( emptySlot's cordinate ) : [( from codinates1 ), (from cordinate2) .... ]}
    def getAllPossibleMoves() -> defaultdict:
        toRet = defaultdict([])
        if depth == 0:
            centerX, centerY = getInitialBoardState()
            return {(centerX, centerY): getCordinates(centerX, centerY)}
        else:
            # remove last move from currentPossibleMoves since poeg moved into slot
            currentPossibleMoves.pop(lastMove[1], None)
            for keys in currentPossibleMoves.keys():
                # Add the possible cordinates from the stay empty slots
                toRet[keys] = getCordinates(keys[0], keys[1])
            # Lastly add empted slot to the possible moves
            toRet[lastMove[0]] = getCordinates(lastMove[0][0], lastMove[0][1])
            return toRet

    # Joowon Suh, Jan, 23
    # Right now it choose only first moves from the possible moves since we didn't added learning feature to AI
    # Onve it choose next move, then it assign combination of from, to cordinates of chosen one to lastMove
    # make the next move
    def selectNextMoveFromDict()-> [(fromX, fromY), (toX, toY)]:
        currentPossibleMoves = getAllPossibleMoves()
        keys = currentPossibleMoves.keys()
        values = currentPossibleMoves.values()
        lastMove = [(values[0][0], values[0][1]), (keys[0], keys[1])]
        return [(values[0][0], values[0][1]), (keys[0], keys[1])]

    # make move with result of selectNextMoveFromDict
    def makeMove():
        pass

    # Joowon Suh, Jan, 23
    # this function is called once when game is started
    # returns a tuple describing coordinate of center peg
    def getInitialBoardState() -> (int, int):
        cols = gameBoard.getCols()
        rows = gameBoard.getRows()
        centerX = math.ceil(cols/2)
        centerY = math.ceil(rows/2)
        return (centerX, centerY)
