'''
Created on Oct 28, 2018

@author: cmins
'''
import psgamestate

# Chan Woo, Jan, 23 moved input functions from psgamestate to main
def getFromInput() -> (int, int):
    while True:
        from_input = input("FROM: ")
        from_input = from_input.split()
        print(from_input)
        if len(from_input) == 2:
            try:
                from_row = int(from_input[0])
                from_col = int(from_input[1])
                # Joowon, Jan, 04 changed it to return coordinate of input instead of set self value and break
                return (from_row, from_col)
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
                # Joowon, Jan, 04 changed it to return coordinate of input instead of set self value and break
                return (to_row, to_col)
            except:
                print("INVALID MOVE")
        else:
            print("INVALID MOVE")


if __name__ == "__main__":
    game = psgamestate.PSGameState()
    game.start()
