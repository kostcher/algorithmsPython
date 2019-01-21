# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение -
# [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

first = deque(input('Введите первое число:'))
second = deque(input('Введите второе число:'))

NUMBERS = '0123456789ABCDEF';
HEX_TABLE = {i: n for n, i in enumerate('0123456789ABCDEF')}


def sum_ab(a: deque, b: deque):
    while len(a) > len(b):
        b.appendleft('0')
    while len(a) < len(b):
        a.appendleft('0')

    result = deque()
    tmp = 0

    for i in range(len(a) - 1, -1, -1):
        tmp = HEX_TABLE[a[i]] + HEX_TABLE[b[i]] + tmp // 16
        result.appendleft(tmp % 16)

        if tmp // 16 and i == 0:
            result.appendleft(tmp // 16)

    return [NUMBERS[number] for number in result]


print(sum_ab(first, second))
