# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = 123

a = number % 10
b = number % 100 // 10
c = number // 100

summ = a + b + c
product = a * b * c

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

# Переменная number имеет размер 14 байт
# Переменная a имеет размер 14 байт
# Переменная b имеет размер 14 байт
# Переменная c имеет размер 14 байт
# Переменная summ имеет размер 14 байт
# Переменная product имеет размер 14 байт
# Общий размер 84 байт
