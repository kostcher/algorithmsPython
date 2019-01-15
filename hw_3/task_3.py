#  В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

numbers = [random.randint(0, 100) for _ in range(10)]

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

numbers[max_number_index], numbers[min_number_index] = min_number, max_number

print(numbers)
