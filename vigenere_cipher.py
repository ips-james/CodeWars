# def caesar(string, n):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     return [''.join(alphabet[(alphabet.index(x)+n) % len(alphabet)]) for x in string]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

def vig(string):
    return [''.join(alphabet[(alphabet.index(x) + n) % len(alphabet)]) for x in string]

def create_vig(key, alphabet):
    helper = [''.join(key[(alphabet.index(x)x for x in range(len(alphabet))]
    return helper

print(create_vig(key, alphabet))



