# Определить, какое число в массиве встречается чаще всего.
# Windows 10, 64 битная, python - 3.6.8
import random
import sys


def get_total_seize(huh):
    """
    Подсчет занимаемой памяти
    """
    total_memory = 0
    for key, value in huh.items():
        total_memory += sys.getsizeof(value)
    return total_memory

# вариант со словарем, после проход словаря в цикле
def test1(n):
    SIZE = n
    MIN_ITEM = 1
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
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

    return get_total_seize(locals())
    

# print(f'Результат на 10: {test1(10)}')
# print(f'Результат на 100: {test1(100)}')
# print(f'Результат на 1000: {test1(1000)}')
# print(f'Результат на 10000: {test1(10000)}')
print(f'Результат на 100000: {test1(100000)}')

# Результат на 10: 784
# Результат на 100: 3416
# Результат на 1000: 13952
# Результат на 10000: 92552
# Результат на 100000: 829392

# вариант через два цикла т.е. берем число и считаем сколько раз оно встречается
def test2(n):
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]

    # вариант 1
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

    return get_total_seize(locals())

# print(f'Результат на 10: {test2(10)}')
# print(f'Результат на 100: {test2(100)}')
# print(f'Результат на 1000: {test2(1000)}')
# print(f'Результат на 10000: {test2(10000)}')
# print(f'Результат на 100000: {test2(100000)}')

# Результат на 10: 440
# Результат на 100: 1160
# Результат на 1000: 9272
# Результат на 10000: 87872
# Результат на 100000: 824712

# вариант со словарем, но убрал проход словаря в цикле
def test3(n):
    SIZE = n
    MIN_ITEM = 0
    MAX_ITEM = 99
    array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item

    return get_total_seize(locals())


# print(f'Результат на 10: {test3(10)}')
# print(f'Результат на 100: {test3(100)}')
# print(f'Результат на 1000: {test3(1000)}')
# print(f'Результат на 10000: {test3(10000)}')
# print(f'Результат на 100000: {test3(100000)}')

# Результат на 10: 752
# Результат на 100: 3384
# Результат на 1000: 13920
# Результат на 10000: 92520
# Результат на 100000: 829360


# Вывод: Первый и третий вариант потребляют почти одинаковое кол-во памяти
# Второй на маленьких данных потребляет значительно меньше, но с увеличением данных разница в памяти становится не большой
# Но скорость выполнения программы во втором варианте сильно снижается. Пока ждал на 100000 весь чай дома и у соседей выпил.
# Исходя из полученных данных лучшим вариантом будет использовать 2 или 3 т.к. высокая скорость и не сильное увеличение занимаемой памяти