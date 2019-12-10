def maxSequence(array):
    total = 0
    old_total = 0
    start = 0
    end = 0
    for x in range(len(array)):
        if x < 0:
            start = x


maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
