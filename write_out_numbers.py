# https://www.codewars.com/kata/write-out-numbers
# Create a function that transforms any positive number to a string
# representing the number in words. The function should work for all numbers between 0 and 999999.
#
# Examples
# number2words(0)  ==>  "zero"
# number2words(1)  ==>  "one"
# number2words(9)  ==>  "nine"
# number2words(10)  ==>  "ten"
# number2words(17)  ==>  "seventeen"
# number2words(20)  ==>  "twenty"
# number2words(21)  ==>  "twenty-one"
# number2words(45)  ==>  "forty-five"
# number2words(80)  ==>  "eighty"
# number2words(99)  ==>  "ninety-nine"
# number2words(100)  ==>  "one hundred"
# number2words(301)  ==>  "three hundred one"
# number2words(799)  ==>  "seven hundred ninety-nine"
# number2words(800)  ==>  "eight hundred"
# number2words(950)  ==>  "nine hundred fifty"
# number2words(1000)  ==>  "one thousand"
# number2words(1002)  ==>  "one thousand two"
# number2words(3051)  ==>  "three thousand fifty-one"
# number2words(7200)  ==>  "seven thousand two hundred"
# number2words(7219)  ==>  "seven thousand two hundred nineteen"
# number2words(8330)  ==>  "eight thousand three hundred thirty"
# number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
# number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred eighty-eight"

from math import log10

minor_words = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
               11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
               15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
major_words = {0: '', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
               90: 'ninety'}


def number2words(n):
    original = n
    parts = []
    answer = []
    size = int(log10(n))
    for x in range(5, -1, -1):
        digit = int(n / (10 ** x))
        parts.append(digit)
        n -= digit * (10 ** x)
    # n = original
    # if n < 100000:
    #     if n < 1000:
    #         if n < 100:
    #             if n < 20:
    #                 return minor_words[n]
    #             else:
    #                 return major_words[parts[0]*10] + '-' + minor_words[parts[1]]
    #         return minor_words[parts[0]] + ' hundred ' + major_words[parts[1]*10] + '-' + minor_words[parts[2]]
    #     return minor_words[parts[0]] + ' thousand ' + minor_words[parts[1]] + ' hundred ' + major_words[parts[2]*10] + '-' + minor_words[parts[3]]
    # return 'many thousands'
    if parts[0] > 0:
        answer.append(minor_words[parts[0]] + ' hundred ')
    if parts[1] > 0:
        answer.append(major_words[parts[1] + minor_words[parts[2]]])


print(number2words(100))
