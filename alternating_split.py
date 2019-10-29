# For building the encrypted string:
# Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
# Do this n times!
#
# Examples:
#
# "This is a test!", 1 -> "hsi  etTi sats!"
# "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"


def encrypt_run(text):
    letters = [x for x in text]
    part1 = ""
    part2 = ""
    for i in range(len(letters)):
        if i % 2 == 0:
            part2 += letters[i]
        else:
            part1 += letters[i]
    return part1 + part2


def encrypt(text, n):
    if n <= 0:
        return text
    else:
        i = n
        while i > 0:
            text = encrypt_run(text)
            i -= 1
    return text


def decrypt_run(text):
    part1 = (text[i] for i in range(int(len(text) / 2)))
    part2 = (text[i] for i in range(int(len(text) / 2), len(text)))
    return part1, part2


print(decrypt_run("This is a test!"))



