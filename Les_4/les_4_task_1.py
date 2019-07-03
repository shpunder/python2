# Определить, какое число в массиве встречается чаще всего.
import random
import cProfile


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

    # print(f'Число {key_position} встречается {max_value} раз')

# les_4_task_1.test1(100)
# 1 100 loops, best of 3: 114 usec per loop
# 2 100 loops, best of 3: 115 usec per loop
# 3 100 loops, best of 3: 114 usec per loop

# les_4_task_1.test1(1000)
# 1 100 loops, best of 3: 1.13 msec per loop
# 2 100 loops, best of 3: 1.12 msec per loop
# 3 100 loops, best of 3: 1.13 msec per loop

# les_4_task_1.test1(10000)
# 1 100 loops, best of 3: 11.2 msec per loop
# 2 100 loops, best of 3: 11.2 msec per loop
# 3 100 loops, best of 3: 11.2 msec per loop

# cProfile.run('test1(100)')
# 1    0.000    0.000    0.001    0.001 les_4_task_1.py:6(test1)
# cProfile.run('test1(1000)')
# 1    0.000    0.000    0.008    0.008 les_4_task_1.py:6(test1)
# cProfile.run('test1(10000)')
# 1    0.003    0.003    0.091    0.091 les_4_task_1.py:6(test1)

# Увеличили SIZE в 10 раз. Время так же увеличилось в 10 раз. Сложность кода O(n)
# Так же при увеличении разницы между MIN_ITEM  и MAX_ITEM увеличивается время прохода словаря т.к. в словаре больше элементов

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

# les_4_task_1.test2(100)
# 1 100 loops, best of 3: 396 usec per loop
# 2 100 loops, best of 3: 402 usec per loop
# 3 100 loops, best of 3: 394 usec per loop

# les_4_task_1.test2(1000)
# 1 100 loops, best of 3: 31.6 msec per loop
# 2 100 loops, best of 3: 32.5 msec per loop
# 3 100 loops, best of 3: 31.8 msec per loop

# les_4_task_1.test2(10000)
# 1 10 loops, best of 3: 3.06 sec per loop
# 2 10 loops, best of 3: 3.09 sec per loop
# 3 10 loops, best of 3: 3.08 sec per loop

# cProfile.run('test2(100)')
# 1    0.002    0.002    0.003    0.003 les_4_task_1.py:53(test2)
# cProfile.run('test2(1000)')
# 1    0.105    0.105    0.114    0.114 les_4_task_1.py:53(test2)
# cProfile.run('test2(10000)')
# 1   10.231   10.231   10.315   10.315 les_4_task_1.py:53(test2)

# Сложность O(n**2)

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

# les_4_task_1.test3(100)
# 1 100 loops, best of 3: 116 usec per loop
# 2 100 loops, best of 3: 117 usec per loop
# 3 100 loops, best of 3: 116 usec per loop

# les_4_task_1.test3(1000)
# 1 100 loops, best of 3: 1.16 msec per loop
# 2 100 loops, best of 3: 1.13 msec per loop
# 3 100 loops, best of 3: 1.15 msec per loop

# les_4_task_1.test3(10000)
# 1 100 loops, best of 3: 11.5 msec per loop
# 2 100 loops, best of 3: 11.5 msec per loop
# 3 100 loops, best of 3: 11.6 msec per loop

# cProfile.run('test3(100)')
# 1    0.000    0.000    0.001    0.001 les_4_task_1.py:96(test3)
# cProfile.run('test3(1000)')
# 1    0.105    0.105    0.114    0.114 les_4_task_1.py:53(test2)
# cProfile.run('test3(10000)')
# 1   10.231   10.231   10.315   10.315 les_4_task_1.py:53(test2)

# сложность O(n)

# Вывод: лучшим вариантом является test1 т.к. у него минимальное время выполнения программы
# так же получается, что пройти в цикле словарь выгоднее, чем каждый раз сравнивать значение.