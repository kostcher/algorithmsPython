# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.

number = int(input('Введите число:'))

result = 0

while number > 0:
    result = result * 10 + number % 10
    number = number // 10

print(result)