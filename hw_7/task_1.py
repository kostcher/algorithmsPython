# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def cocktail_sort(array):
    left = 0
    right = len(array) - 1

    while left <= right:
        for i in range(left, right):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        right -= 1

        for i in range(right, left, -1):
            if array[i + 1] < array[i]:
                array[i], array[i - 1] = array[i - 1], array[i]

        left += 1

    return array


array = [random.randint(-100, 99) for i in range(10)]

print(array)
print(cocktail_sort(array))
