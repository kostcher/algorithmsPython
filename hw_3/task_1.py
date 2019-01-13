# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

result = {}

for divider in range(2, 10):
    result[divider] = 0

    for dividend in range(2, 100):
        if dividend % divider == 0:
            result[divider] += 1

print('В диапазоне 2 - 99:')
for divider, count in result.items():
    print(f'Количество чисел кратных {divider} -> {count}')
