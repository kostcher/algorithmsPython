# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

first_letter = input('Введите первую букву:')
second_letter = input('Введите вторую букву:')

first_letter_in_alph = ord(first_letter) - (ord('a') - 1)
second_letter_in_alph = ord(second_letter) - (ord('a') - 1)
dist_between_letters = abs(second_letter_in_alph - first_letter_in_alph)

if dist_between_letters != 0:
    dist_between_letters -= 1

print(f'Буква {first_letter} в алфавите №{first_letter_in_alph}')
print(f'Буква {second_letter} в алфавите №{second_letter_in_alph}')
print(f'Между буквой \'{first_letter}\' и \'{second_letter}\' {dist_between_letters} букв')
