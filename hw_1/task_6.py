# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_number = int(input('Введите номер буквы в латинском алфавите:'))

letter = chr(letter_number + (ord('a') - 1))

print(letter)