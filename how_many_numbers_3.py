# https://www.codewars.com/kata/5877e7d568909e5ff90017e6
#
# We want to generate all the numbers of three digits where:
#
# the sum of their digits is equal to 10.
#
# their digits are in increasing order (the numbers may have two or more equal contiguous digits)
#
# The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334
#
# Make a function that receives two arguments:
#
# the sum of digits value
#
# the desired number of digits for the numbers
#
# The function should output an array with three values: [1,2,3]
#
# 1 - the total number of possible numbers
#
# 2 - the minimum number
#
# 3 - the maximum number
#
# The example given above should be:
#
# find_all(10, 3) == [8, 118, 334]
# If we have only one possible number as a solution, it should output a result like the one below:
#
# find_all(27, 3) == [1, 999, 999]
# If there are no possible numbers, the function should output the empty array.
#
# find_all(84, 4) == []
# The number of solutions climbs up when the number of digits increases.
#
# find_all(35, 6) == [123, 116999, 566666]

# todo: find a better way than generating all the numbers


# def find_all(desired_sum, digits):
#     hits = []
#     lower_limit = 10 ** (digits-1)
#     upper_limit = 10 ** digits
#     for x in range(lower_limit, upper_limit):
#         count = 0
#         for i in str(x):
#             count += int(i)
#         if count == desired_sum:
#             hits.append(x)
#     hits = [x for x in hits if check_digits(x)]
#     if not hits:
#         return []
#     return [len(hits), min(hits), max(hits)]
#
#
# def check_digits(n):
#     for x in range(1, len(str(n))):
#         if int(str(n)[x-1]) > int(str(n)[x]):
#             return False
#     return True

from itertools import combinations_with_replacement


def find_all(sum_of_digits, digits):
    # create the set of all numbers where the digits are increasing
    # https://docs.python.org/3.1/library/itertools.html#itertools.combinations_with_replacement
    # this is similar to using product() and then removing entries which aren't in the correct order
    set_c = combinations_with_replacement(list(range(1, 10)), digits)

    target = [''.join(str(x) for x in list(i)) for i in set_c if sum(i) == sum_of_digits]
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]


print(find_all(19, 3))
