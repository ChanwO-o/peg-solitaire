from collections import defaultdict
import psgamestate
import psboard

class AI:

    state = defaultdict()
    depth = 1
    gamestate = psgamestate.PSGameState()
    gameboard = psboard.psBoard()

    # get coordinates of pegs which can be moved into current coordinate
    def getCoordinates(r, c) -> [(int,int)]:
        pass

    # get all possible moves from current game state
    def getAllPossibleMoves() -> defaultdict:
        pass

    # make the next move
    def selectNextMoveFromDict():
        pass

    # this function is called once when game is started
    # returns a tuple describing coordinate of center peg
    def getInitialBoardState() -> (int, int):
        pass
