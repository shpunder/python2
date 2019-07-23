# 2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.
import random

array = [round(random.uniform(0, 50), 2) for i in range(11)]


def merge(arr1,arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:]
    result += arr2[j:]

    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    arr1 = merge_sort(array[:len(array) // 2])
    arr2 = merge_sort(array[len(array) // 2:])

    return merge(arr1, arr2)


print(array)
print(merge_sort(array))

