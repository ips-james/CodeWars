# https://www.codewars.com/kata/5541f58a944b85ce6d00006a
#
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
#
# F(n) * F(n+1) = prod.
#
# Your function productFib takes an integer (prod) and returns an array:
#
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)


def fib(limit: float):
    results = [1]
    n1 = 1
    for x in range(1, int(limit)):
        results.append(n1)
        n1 = n1 + results[x - 1]
    return results


def productFib(i: int):
    results = fib(i * 2)
    for x in range(1, len(results)):
        a = results[x]
        b = results[x-1]
        if a * b == i:
            print([i, b, a, True])
            return [b, a, True]
        if a * b > i:
            print([i, b, a, False])
            return [b, a, False]




