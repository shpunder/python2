# В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random


SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 9
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

min_1 = MAX_ITEM
min_2 = MAX_ITEM

for item in array:
    if item < min_1:
        if min_2 > min_1:
            min_2 = min_1
        min_1 = item
    elif item < min_2:
        min_2 = item


print(f'Первое минимальное число {min_1} второе {min_2}')


