# Определить, является ли год, который ввел пользователем, високосным или не високосным

year = int(input('Введите год: '))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(f'{year} не високосным год')
else:
    print(f'{year} високосным год')