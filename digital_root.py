# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If
# that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is
# only applicable to the natural numbers.


def digital_root(n):
    answer = 0
    for i in range(len(str(n))):
        answer += int(str(n)[i])
    if len(str(answer)) > 1:
        return digital_root(answer)
    else:
        return answer


print(digital_root(14654187184164315419))
