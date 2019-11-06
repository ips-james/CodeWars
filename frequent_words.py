# incomplete
# https://www.codewars.com/kata/most-frequently-used-words-in-a-text/train/python
import re


def top_3_words(input_string):
    word_list = re.findall(r'\s?(\s*\S+)', input_string)
    count_list = [input_string.count(x) for x in word_list]
    answerlist = dict(zip(word_list, count_list))
    result = (sorted(answerlist.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
    return result
    # return list([result[0][0], result[1][0], result[2][0]])


print(top_3_words('In a village of La Mancha, the name of which I have no desire to call to'
                  'mind, there lived not long since one of those gentlemen that keep a lance'
                  'in the lance-rack, an old buckler, a lean hack, and a greyhound for'
                  'coursing. An olla of rather more beef than mutton, a salad on most'
                  'nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra'
                  'on Sundays, made away with three-quarters of his income.'))  # ["a", "of", "on"])

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))  # ["e", "d", "a"]))
