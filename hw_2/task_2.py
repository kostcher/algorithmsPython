# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Введите натуральное число:'))

event_cnt = 0
not_event_cnt = 0

while number > 0:
    last_number = number % 10
    number = number // 10

    if last_number % 2 == 0:
        event_cnt += 1
    else:
        not_event_cnt += 1

print(f'В введенном числе кол-во четных чисел {event_cnt} нечетных {not_event_cnt}')
