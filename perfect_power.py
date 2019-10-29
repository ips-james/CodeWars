from math import log, sqrt


def isPP(num):
    for i in range(2, 40):
        power = round(num ** (1 / i), 6)
        if round(power) == power:
            return [round(power), i]

# def isPP(n):
#     n = int(n)
#     if n < 4:
#         return None
#     sr = round(sqrt(n), 6)
#     if sr == round(sr):
#         return [sr, 2]
#     for m in range(2, int(n / 2)):
#         k = round(log(n, m), 6)
#         if k == round(k):
#             return [m, round(k)]
#     return None


print(isPP(12167))
