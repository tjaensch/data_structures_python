MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '&': '.-...',
    '@': '.--.-.',
    ':': '---...',
    ',': '--..--',
    '.': '.-.-.-',
    ''': '.----.',
    ''': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '!': '-.-.--',
}

MORSE_CODE_REVERSED = {val: key for key, val in MORSE_CODE.items()}

class MorseCode:

    def __init__(self):
        self.morse_code_dict = MORSE_CODE
        self.morse_code_reversed_dict = MORSE_CODE_REVERSED

    @staticmethod
    def encrypt(message):
      return ' '.join([MORSE_CODE[char.upper()] if char != ' ' else '/' for char in message])
  
    @staticmethod
    def decrypt(message):
      return ''.join([MORSE_CODE_REVERSED[char] if char != '/' else ' ' for char in message.split()])


if __name__ == '__main__':
    morse_code = MorseCode()
    print(morse_code.encrypt('Hello World'))
    print(morse_code.decrypt('.... . .-.. .-.. --- / .-- --- .-. .-.. -..'))