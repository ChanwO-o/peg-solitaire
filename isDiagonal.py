def isDiagonal(fromcol: int, fromrow: int, tocol: int, torow: int) -> bool:
    if (fromcol - tocol) != 0 and (fromrow - torow) != 0:
        raise PSInvalidMoveException()
    return True
