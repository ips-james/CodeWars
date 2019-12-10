from math import log10

codes = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'gray': 8,
         'white': 9}
tolerances = {'gold': '5%', 'silver': '10%'}


def decode_resistor_colors(bands):
    resistances = list(bands.split(' '))
    total = ((codes[resistances[0]] * 10) + (codes[resistances[1]])) * (10 ** codes[resistances[2]])
    answer = str(total)
    if total >= 1000000:
        if (total / 1000000) % 1 == 0:
            answer = str(int((total / 1000000))) + 'M'
        else:
            answer = str(round((total / 1000000), 1)) + 'M'
    elif 1000 <= total < 1000000:
        if (total / 1000) % 1 == 0:
            answer = str(int(total / 1000)) + 'k'
        else:
            answer = str(round((total / 1000), 1)) + 'k'
    if len(resistances) == 4:
        tolerance = tolerances[resistances[3]]
    else:
        tolerance = '20%'
    return answer + ' ohms, ' + tolerance


def encode_resistor_colors(ohms_string):
    inv_map = {v: k for k, v in codes.items()}
    resistance = ohms_string.split(' ')[0]
    if resistance.endswith('M'):
        value = float(resistance[:-1]) * (10 ** 6)
    elif resistance.endswith('k'):
        value = float(resistance[:-1]) * (10 ** 3)
    else:
        value = float(resistance)
    multiplier = int(log10(value)) - 1
    first_digit = int(str(value)[0])
    second_digit = int(str(value)[1])
    return inv_map[first_digit] + ' ' + inv_map[second_digit] + ' ' + inv_map[multiplier] + ' gold'


print(encode_resistor_colors('47k ohms'))

