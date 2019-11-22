from morse_code1 import decodeMorse

# todo: Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore
#  them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.


def decodeBits(bits):
    count = 0
    max_zero = 0
    for x in bits:
        if x == '0':
            count += 1
        if x == '1':
            if count > max_zero:
                max_zero = count
            count = 0
    time_series = max_zero // 7
    if time_series == 0:
        for x in bits:
            if x == '1':
                count += 1
            if x == '0':
                if count > max_zero:
                    max_zero = count
                count = 0
        time_series = max_zero // 7
    if time_series == 0:
        time_series = 1
    bits = bits.replace('0' * 7 * time_series, '   ')
    bits = bits.replace('0' * 3 * time_series, ' ')
    bits = bits.replace('1' * 3 * time_series, '-')
    bits = bits.replace('1' * 1 * time_series, '.')
    bits = bits.replace('0' * 1 * time_series, '')
    return bits


test_bits = '111'


print(decodeMorse(decodeBits(test_bits)))
