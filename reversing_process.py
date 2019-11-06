import re


def decode(string):
    results = re.findall('([\\d]+)([\\D]+)', string)
    coded_text = str(results[0][1])
    shift = int(results[0][0])
    return_string = ''.join(ord(x) for x in coded_text)
    return return_string


ts = '6015ekx'

print(decode(ts))
print(ord('a'))
