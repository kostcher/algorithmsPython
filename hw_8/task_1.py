# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

import random

string_len = random.randint(2, 100)
string = ''.join([chr(random.randint(97, 122)) for index in range(string_len)])
substrings = set()

stop_plus = 0
for i in range(string_len):
    start = i
    if i == string_len - 2:
        start = i - 1
        stop_plus = 1

    for j in range(i + 1, string_len):
        substrings.add(hash(string[start:j + stop_plus]))

print('Кол-во подстрок: ', len(substrings))
