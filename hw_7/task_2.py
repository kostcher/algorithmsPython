# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(array):
    length = len(array)

    if length <= 1:
        return array

    middle = int(length / 2)
    result = merge(merge_sort(array[:middle]), merge_sort(array[middle:]))

    return result


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right

    return result


source_array = [round(random.uniform(0, 49), 3) for i in range(5)]

print(source_array)
print(merge_sort(source_array))
