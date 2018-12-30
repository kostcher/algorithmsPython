# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов'))
sum_range = 0

if n != 0:
    number = 1
    sum_range = number
    while n > 1:
        number = number * -0.5
        sum_range += number
        n = n - 1

print(f'Сумма элементов равна: {sum_range}')
