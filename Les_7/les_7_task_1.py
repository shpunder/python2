# 1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random

array = [random.randint(-100, 99) for i in range(10)]

def bubble_sort(array):
    n = 1
    flag = True # если обменов не было за проход, то смысла дальше проходить нет
    k = 1 # запомним где был последний обмен
    while n < len(array) and flag:
        flag = False
        for i in range(len(array) - k):
            if array[i] < array[i + 1]:
                flag = True
                k = i
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array

print(array)
print(bubble_sort(array))
