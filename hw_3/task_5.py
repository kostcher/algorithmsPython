# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

numbers = [random.randint(-100, 100) for _ in range(10)]
max_negative_number = 0
max_negative_index = 0

for index, number in enumerate(numbers):
    if number < 0:
        if max_negative_number == 0:
            max_negative_number, max_negative_index = number, index
        elif max_negative_number < number:
            max_negative_number, max_negative_index = number, index

print(numbers)

if max_negative_number != 0:
    print(f'Максимальное отрицательное число {max_negative_number} его индекс {max_negative_index}')
else:
    print('В массиве нет отрицательных чисел')
