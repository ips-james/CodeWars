import string


def caesar(input_string, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    out = input_string.translate(str.maketrans("", "", string.punctuation))
    return ''.join([(alphabet[(alphabet.index(x) - n) % len(alphabet)]) for x in
                    out.lower()])


def decode(message, n):
    decoded_message = []
    for x in message.split(' '):
        decoded_message.append(caesar(x, n))
    return ' '.join(decoded_message)


print(decode('btwqi hello', 5))
