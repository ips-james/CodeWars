# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
# untouched.


def pig_it(text):
    word_list = text.split(' ')
    answer = []
    for word in word_list:
        if not word.isalpha():
            answer.append(word)
        else:
            new_word = word[1:] + word[0] + 'ay'
            answer.append(new_word)
    return ' '.join(answer)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))

# Only works if there is a space before the punctuation.
