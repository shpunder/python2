# Определить, какое число в массиве встречается чаще всего.
import random


SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 3
array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

dict_result = {}

for item in array:
    if item in dict_result:
        dict_result[item] += 1
    else:
        dict_result[item] = 1

max_value = 0
key_position = 0

for key in dict_result:
    if max_value < dict_result[key]:
        max_value = dict_result[key]
        key_position = key

print(f'Число {key_position} встречается {max_value} раз')


