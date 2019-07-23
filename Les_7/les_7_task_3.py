
# 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. 
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

M = 5
array = [random.randint(0, 99) for i in range(M * 2 + 1)]


def gnome_sort(array):
    i = 1
    while i < len(array):
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array


print(array)
gnome_sort(array)
print(array)
print(f'Медиана = {array[len(array) // 2] }')


# для проверки, что правильно нашел медиану
import statistics
print(statistics.median(array))

