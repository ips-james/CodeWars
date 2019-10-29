# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
# differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check
# his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a
# position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1
# (not 0)


def iq_test(numbers):
    numbers_list = numbers.split(' ')
    odd_or_even = 0
    answer = 0
    for x in numbers_list:
        odd_or_even += int(x) % 2
    if odd_or_even == 1:
        for n in range(len(numbers_list)):
            if int(numbers_list[n]) % 2 == 1:
                answer = n
    else:
        for n in range(len(numbers_list)):
            if int(numbers_list[n]) % 2 == 0:
                answer = n
    return answer + 1


print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))

# could have used index() to get the index of the entry in the list.
