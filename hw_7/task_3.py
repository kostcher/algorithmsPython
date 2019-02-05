# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это
# слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


def gnome_sort(array):
    tmp_array = array[:]
    i = 1

    while i < len(tmp_array):
        if not i or tmp_array[i - 1] <= tmp_array[i]:
            i += 1
        else:
            tmp_array[i], tmp_array[i - 1] = tmp_array[i - 1], tmp_array[i]
            i -= 1

    return tmp_array


source_array = [random.randint(0, 49) for i in range(random.randrange(3, 15, 2))]
result_array = gnome_sort(source_array)

print(source_array)
print(result_array)
print('Индекс медианы: ', len(result_array) // 2)
