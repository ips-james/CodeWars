# https://www.codewars.com/kata/moving-zeros-to-the-end/python
#
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
# elements.
#
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
from itertools import repeat

# todo: could instead create two lists and then combine them with the + operator
# todo: rather than creating one array and adding a counted number of zeros on the end


def move_zeros(array):
    tick = 0
    cache = []
    for x in array:
        if x is not 0:
            if x == 0:
                tick +=1
                continue
            cache.append(x)
        else:
            tick += 1
    array = cache
    array.extend(repeat(0, tick))
    return array


print(move_zeros([False, 1, 0.0, 1, 2, 0, 1, 3, "a"]))
