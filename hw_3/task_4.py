# Определить, какое число в массиве встречается чаще всего.

import random

numbers = [random.randint(1, 10) for _ in range(100)]
repeat_numbers = {}

for number in numbers:
    if number not in repeat_numbers:
        repeat_numbers[number] = 1
    else:
        repeat_numbers[number] += 1

max_repeat_number = 0
max_repeat_cnt = 0

for number, repeat_cnt in repeat_numbers.items():
    if repeat_cnt > max_repeat_cnt:
        max_repeat_number, max_repeat_cnt = number, repeat_cnt

if len(numbers) > 1 and max_repeat_cnt == 1:
    print('Все числа в массиве, встречаются не более 1-го раза')
else:
    print(f'Число {max_repeat_number} в массиве встречается чаще всего')
