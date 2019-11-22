# https://www.codewars.com/kata/5659c6d896bc135c4c00021e
# Write a function that takes a positive integer and returns
# the next smaller positive integer containing the same digits.
#
# For example:
#
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017

# todo: find a better algorithm, this only works sensibly for n < 10^10

import itertools


def next_smaller(n):
    answer = []
    answer_set = list(itertools.permutations(str(n), len(str(n))))
    for x in answer_set:
        if int(''.join(x)) < n:
            answer.append(int(''.join(x)))
    try:
        lower_val = max(answer)
    except ValueError:
        return -1
    return lower_val


print(next_smaller(9000000001))
