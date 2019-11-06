# https://www.codewars.com/kata/best-travel

from itertools import combinations


def choose_best_sum(distance, towns, input_array):
    return max((sum(i) for i in combinations(input_array, towns) if sum(i) <= distance), default=None)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

print(choose_best_sum(230, 4, xs))  # 230
print(choose_best_sum(430, 5, xs))  # 430
print(choose_best_sum(430, 8, xs))  # None
