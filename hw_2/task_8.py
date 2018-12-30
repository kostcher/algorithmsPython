# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
# и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

count_input_numbers = int(input('Сколько чисел вы хотите ввести:'))
search_number = int(input('Введите цифру, которую нужно искать:'))

counter = 0

for i in range(count_input_numbers):
    number = int(input(f'Введите число №{i+1}:'))

    while number > 0:
        last_number = number % 10
        number = number // 10

        if last_number == search_number:
            counter += 1

print(f'Цифра {search_number} в введенных числах нашлась {counter} раз')
