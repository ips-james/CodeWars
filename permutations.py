# In this kata you have to create all permutations of an input string and remove duplicates, if present. This means,
# you have to shuffle all letters from the input in all possible orders.
#
# Examples:
#
# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# The order of the permutations doesn't matter.

import itertools


def permutations(word):
    word_list = [''.join(x) for x in itertools.permutations(word)]
    return list(set(word_list))


print(permutations('aabb'))  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
