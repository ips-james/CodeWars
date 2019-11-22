# # https://www.codewars.com/kata/coloured-triangles
#
# A coloured triangle is created from a row of colours, each of which is red, green or blue. Successive rows,
# each containing one fewer colour than the last, are generated by considering the two touching colours in the
# previous row. If these colours are identical, the same colour is used in the new row. If they are different,
# the missing colour is used in the new row. This is continued until the final row, with only a single colour,
# is generated. You will be given the first row of the triangle as a string and its your job to return the final
# colour which would appear in the bottom row as a string. In the case of the example above, you would the given
# RRGBRGBB you should return G.

# TODO: a better solution would be to use a dictionary for the inputs and outputs, rather than a load of if statements


def reduce_row(row: str):
    result = []
    for x in range(len(row)-1):
        if row[x] == row[x+1]:
            result.append(row[x])
        if (row[x] == 'R' and row[x+1] == "G") or (row[x] == 'G' and row[x+1] == "R"):
            result.append('B')
        if (row[x] == 'G' and row[x+1] == "B") or (row[x] == 'B' and row[x+1] == "G"):
            result.append('R')
        if (row[x] == 'B' and row[x+1] == "R") or (row[x] == 'R' and row[x+1] == "B"):
            result.append('G')
    # print(''.join(result))
    return ''.join(result)


def triangle(row: str):
    if len(row) == 1:
        return row
    else:
        return triangle(reduce_row(row))


print(triangle('RRGBRBGBGGGGBBBRBBBBGGBRBRGBGGRRBRBGGBRGGBBBRBGGRGRRGGRBG'))