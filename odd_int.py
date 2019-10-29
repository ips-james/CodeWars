# Given an array, find the int that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.

from collections import Counter


def find_it(seq):
    counts = Counter(seq)
    for i in counts:
        if not((counts[i] / 2).is_integer()):
            return i


test_list = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]

print(find_it(test_list))
