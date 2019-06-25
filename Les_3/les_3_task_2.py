# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
import random


SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

max_position = 0
min_position = 0

for i in range(SIZE):
    if array[i] > array[max_position]:
        max_position = i
    if array[i] < array[min_position]:
        min_position = i

array[max_position], array[min_position] = array[min_position], array[max_position] 

print(array)



