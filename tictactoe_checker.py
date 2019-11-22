# https://www.codewars.com/kata/tic-tac-toe-checker/ If we were to set up a Tic-Tac-Toe game, we would want to know
# whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for
# us!
#
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X",
# or 2 if it is an "O", like so:
#
# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:
#
# -1 if the board is not yet finished (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.


def isSolved(board):
    # check horizontal
    for x in range(3):
        if board[x] == [1, 1, 1]:
            return 1
        if board[x] == [2, 2, 2]:
            return 2
    # check vertical
    for x in range(3):
        if [board[0][x], board[1][x], board[2][x]] == [1, 1, 1]:
            return 1
        if [board[0][x], board[1][x], board[2][x]] == [2, 2, 2]:
            return 2
    # check diagonal TLBR
    if [board[0][0], board[1][1], board[2][2]] == [1, 1, 1]:
        return 1
    if [board[0][0], board[1][1], board[2][2]] == [2, 2, 2]:
        return 2
    # check diagonal TRBL
    if [board[2][0], board[1][1], board[0][2]] == [1, 1, 1]:
        return 1
    if [board[2][0], board[1][1], board[0][2]] == [2, 2, 2]:
        return 2
    # check empty cells
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return -1
    # otherwise draw
    return 0


test_board = [[0, 0, 1],
              [0, 1, 2],
              [2, 1, 0]]

print(isSolved(test_board))

# solution could be made better by combining checks for 1 or 2
