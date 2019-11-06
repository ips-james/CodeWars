# Implement the Polybius square cipher.
#
# Replace every letter with a two digit number. The first digit is the row number, and the second digit is the column
# number of following square. Letters 'I' and 'J' are both 24 in this cipher:
#
# 1	2	3	4	5
# 1	A	B	C	D	E
# 2	F	G	H	I/J	K
# 3	L	M	N	O	P
# 4	Q	R	S	T	U
# 5	V	W	X	Y	Z
# Input will be valid (only spaces and uppercase letters from A to Z), so no need to validate them.
#
# Examples
# polybius('A')  # "11"
# polybius('IJ') # "2424"
# polybius('CODEWARS') # "1334141552114243"
# polybius('POLYBIUS SQUARE CIPHER') # "3534315412244543 434145114215 132435231542"


def polybius(input_string):
    row_mapping = ('ABCDE', 'FGHIJK', 'LMNOP', 'QRSTU', 'VWXYZ')
    column_mapping = ('AFLQV', 'BGMRW', 'CHNSX', 'DIJOTY', 'EKPUZ')
    return_string = ''
    for x in input_string:
        if x == ' ':
            return_string += ' '
        for i in range(len(row_mapping)):
            if x in row_mapping[i]:
                return_string += str(i+1)
        for j in range(len(row_mapping)):
            if x in column_mapping[j]:
                return_string += str(j+1)
    return return_string


print(polybius('POLYBIUS SQUARE CIPHER'))
