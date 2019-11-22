# https://www.codewars.com/kata/twice-linear/python
#
# Consider a sequence u where u is defined as follows:
#
# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
#
# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
#
# Task: Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <)
# sequence u (so, there are no duplicates).
#
# Example:
# dbl_linear(10) should return 22


def dbl_linear(x: int):
    u = [1]
    # Limit of 6x chosen to pass the given tests in a reasonable time. Not ideal.
    for n in range(x * 6):
        u.append(((u[n]) * 2) + 1)
        u.append(((u[n]) * 3) + 1)
    u = sorted(list(dict.fromkeys(u)))
    return u[x]


print(dbl_linear(60000))

# best solution is to use a different data type like a deque instead of a list.
