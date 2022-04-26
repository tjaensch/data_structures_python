#https://www.udemy.com/course/advanced-exercises-python-programming/learn/quiz/5222098#overview

import string

def generate_cipher(alph, key=2):

  alph_substr = alph[:key]

  new_alph = alph[key:] + alph_substr

  return new_alph


print(generate_cipher(string.ascii_lowercase,3))