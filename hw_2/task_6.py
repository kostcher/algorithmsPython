# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

conceived_number = random.randint(0, 100)
is_guess_number = False
cnt_number_attempts = 10

while cnt_number_attempts > 0 and not is_guess_number:
    input_number = int(input('Введите целое число'))

    if input_number == conceived_number:
        is_guess_number = True
    elif input_number > conceived_number:
        print('Введенное число больше загаданного')
    else:
        print('Введенное число меньше загаданного')

    cnt_number_attempts -= 1

if is_guess_number:
    print('Вы выйграли')
else:
    print(f'Вы проиграли. \nЗагаданное число {conceived_number}')
