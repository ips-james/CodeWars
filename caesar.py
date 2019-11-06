def caesar(string, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([(alphabet[(alphabet.index(x)-n) % len(alphabet)]) for x in string.lower()])


print(caesar('btwqi', 5))
