# You are given a string representing a website's address. To calculate the IP address you must convert all the
# characters into ASCII code, then calculate the sum of the values.
#
# The first IP number will be the result mod 256. The second IP number will be the double of the sum mod 256,
# the third will be the triple of the sum mod 256 and the fourth will be quadruple of the sum, mod 256.
#
# Input :
# A string representing the website address
#
# Output
# An array containing the IP value
#
# Examples :
# f('www.codewars.com')   ---> [88, 176, 8, 96]
# f('www.starwiki.com')   ---> [110, 220, 74, 184]
# Restrictions :
# Code length: <= 59 characters
# "import" is forbidden as a part of anti-cheat

# Code length = 88, just 29 to go


def f(a):
    m = sum([ord(x) for x in a])
    return [m%256, m*2%256, m*3%256, m*4%256]

