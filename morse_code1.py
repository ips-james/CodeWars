# https://www.codewars.com/kata/decode-the-morse-code/python

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
              '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
              '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
              '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

# todo: use strip() to remove whitespace, therefore removing the need to skip empty words or letters


def decodeMorse(morse_code):
    answer = []
    words = morse_code.split('   ')
    for word in words:
        if word == '':
            continue
        letters = word.split(' ')
        for letter in letters:
            if letter == '':
                continue
            answer.append(MORSE_CODE[letter])
        answer.append(' ')
    answer.pop()
    return ''.join(answer)


