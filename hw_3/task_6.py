# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

numbers = [random.randint(-0, 100) for _ in range(10)]

max_number = 0
min_number = 0
max_number_index = 0
min_number_index = 0

for i, number in enumerate(numbers):
    if i == 0:
        max_number, min_number = number, number
    else:
        if number > max_number:
            max_number, max_number_index = number, i
        elif number < min_number:
            min_number, min_number_index = number, i

start, stop = max_number_index, min_number_index
if min_number_index < max_number_index:
    start, stop = min_number_index, max_number_index

sum_numbers = 0

if stop - start != 1:
    for index in range(start + 1, stop):
        sum_numbers += numbers[index]

    print(f'Сумма элементов, находящихся между минимальным и максимальным элементами равна: {sum_numbers}')
else:
    print('Между минимальным и максимальным элементом нет чисел')
