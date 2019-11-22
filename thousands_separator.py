# https://pythonprinciples.com/challenges/Thousands-separator/
#
# Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.
#
# Your function should convert the number to a string and add commas as a thousands separator.
#
# For example, calling format_number(1000000) should return "1,000,000".

import math


def format_number(n):
    string = list(str(n))
    commas = []
    shift = 0
    # how many commas will we need?
    number_of_commas = math.trunc(math.log10(n)/3)
    # create a list of which digits the commas will separate
    for x in range(number_of_commas):
        commas.append(len(str(n)) - 3*(x+1))
    # insert the commas into the string, remembering to add another index position for each comma we have added
    # previously
    for i in reversed(commas):
        string.insert(i+shift, ',')
        shift += 1
    return ''.join(string)


print(format_number(1239265784456789))
