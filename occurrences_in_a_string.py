# https://www.codewars.com/kata/count-and-group-character-occurrences-in-a-string/python
#
# Write a method that takes a string as an argument and groups the number of time each character appears in the
# string as a hash sorted by the highest number of occurrences.
#
# The characters should be sorted alphabetically e.g:
#
# get_char_count("cba") == {1: ["a", "b", "c"]}
# You should ignore spaces, special characters and count uppercase letters as lowercase ones.
#
# For example:
#
# get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}

import string


def get_char_count(input_string: str):
    # strip the punctuation using a translation, also turn everything lowercase
    translator = str.maketrans('', '', string.punctuation)
    lower_string = input_string.lower()
    stripped = lower_string.translate(translator)
    # create a dictionary with the letter counts
    count_dict = {x: stripped.count(x) for x in stripped}
    count_dict.pop(' ', None)
    # group the dictionary by count number. setdefault initialises a new list for each new letter
    result = {}
    for key, value in sorted(count_dict.items(),):
        result.setdefault(value, []).append(key)
    return result


print(get_char_count('Hello. Hello? HELLO!'))
