# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys
import random

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

count_input_numbers = 2

sum_digits_number = 0
max_number = 0

if count_input_numbers > 0:
    for i in range(count_input_numbers):
        number = random.randint(1, 100)

        tmp_sum_digits_number = 0
        tmp_number = number

        while number > 0:
            last_number = number % 10
            number = number // 10

            tmp_sum_digits_number += last_number

        if tmp_sum_digits_number > sum_digits_number:
            sum_digits_number = tmp_sum_digits_number
            max_number = tmp_number

# print(f'У числа {max_number} иаксимальная сумма чисел среди введенных, его сумма равна {sum_digits_number}')

# print(f"Сумма цифр числа: {summ}")
# print(f"Произведение цифр числа: {product}")


def variables_sizes():
    sizes_vars = {}
    default_types = [int, float, complex, list, tuple, range, str, bytes,
                     bytearray, memoryview, set, frozenset, dict]

    for name, val in list(globals().items()):
        if not name.startswith('__'):
            for default_type in default_types:
                if isinstance(val, default_type):
                    sizes_vars[name] = sys.getsizeof(val)

    return sizes_vars


variables_sizes = variables_sizes().items()

total_size = 0
for var, size in variables_sizes:
    print(f'Переменная {var} имеет размер {size} байт')
    total_size += size

print(f'Общий размер {total_size} байт')

# Переменная count_input_numbers имеет размер 14 байт
# Переменная sum_digits_number имеет размер 14 байт
# Переменная max_number имеет размер 14 байт
# Переменная i имеет размер 14 байт
# Переменная number имеет размер 12 байт
# Переменная tmp_sum_digits_number имеет размер 14 байт
# Переменная tmp_number имеет размер 14 байт
# Переменная last_number имеет размер 14 байт
# Общий размер 110 байт
