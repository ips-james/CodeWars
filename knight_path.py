# https://www.codewars.com/kata/549ee8b47111a81214000941
#
# Given two different positions on a chess board, find the least number of moves it would take a knight to get from
# one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3",
# "b5") should return 1.
#
# The knight is not allowed to move off the board. The board is 8x8.

column_indices = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
board_size = 8


class cell:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


def notation_to_xy(notation: str):
    x = column_indices.index(notation[0]) + 1
    y = int(notation[1])
    return [x, y]

# unused:
# def xy_to_notation(position: list):
#     return column_indices[position[0] - 1] + str(position[1])


# check whether position is valid
def valid_position(x, y):
    if 1 <= x <= board_size and 1 <= y <= board_size:
        return True
    return False


def knight(kp, dest):
    knight_position = notation_to_xy(kp)
    destination = notation_to_xy(dest)

    # define possible knight movements
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = [cell(knight_position[0], knight_position[1], 0)]

    # create an array representing squares on the board, and mark all as unvisited
    visited = [[False for i in range(board_size + 1)] for j in range(board_size + 1)]

    # mark starting square as visited
    visited[knight_position[0]][knight_position[1]] = True

    # loop until we have one element in queue
    while len(queue) > 0:

        t = queue[0]
        queue.pop(0)

        # if current cell is equal to target, return its distance
        if t.x == destination[0] and t.y == destination[1]:
            return t.dist

        # iterate over all possible moves
        for i in range(8):

            x = t.x + dx[i]
            y = t.y + dy[i]

            if valid_position(x, y) and not visited[x][y]:
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))
