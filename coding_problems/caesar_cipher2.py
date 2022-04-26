#https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5222114#overview

import string

def generate_cipher(alphabet, key=2):
    cipher = ''
    for letter in alphabet:
        new_idx = (alphabet.index(letter) + key) % len(alphabet)
        cipher += alphabet[new_idx]
    return cipher


def encrypt(alphabet, message, key):
    cipher = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            result += cipher[alphabet.index(letter)]
    return result


# make key negative
def decrypt_simple(alphabet, message, key):
    key = (-1) * key
    return encrypt(alphabet, message, key)


def decrypt(alphabet, message, key):
  orig_alph = string.ascii_lowercase
  result = ''
  for letter in message:
    if letter not in orig_alph:
      result += letter
    else:
      result += alphabet[orig_alph.index(letter)-key]
  return result


print(encrypt(string.ascii_lowercase, 'jesus christ!', 3))
print(decrypt(string.ascii_lowercase, 'mhvxv fkulvw!', 3))
print(decrypt(string.ascii_lowercase, 'fgbc gur nggnpx!', 13))
print(decrypt_simple(string.ascii_lowercase, 'fgbc gur nggnpx!', 13))