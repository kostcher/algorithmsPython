# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

count_input_numbers = int(input('Сколько чисел вы хотите ввести:'))

sum_digits_number = 0
max_number = 0

if count_input_numbers > 0:
    for i in range(count_input_numbers):
        number = int(input(f'Введите целое натуральное число №{i+1}:'))

        tmp_sum_digits_number = 0
        tmp_number = number

        while number > 0:
            last_number = number % 10
            number = number // 10

            tmp_sum_digits_number += last_number

        if tmp_sum_digits_number > sum_digits_number:
            sum_digits_number = tmp_sum_digits_number
            max_number = tmp_number

print(f'У числа {max_number} иаксимальная сумма чисел среди введенных, его сумма равна {sum_digits_number}')
