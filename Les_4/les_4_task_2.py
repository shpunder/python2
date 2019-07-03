# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(100, 5)"
# Написать два алгоритма нахождения i-го по счёту простого числа.
import random
import cProfile
from math import sqrt

def sieve(size, n):
    MAX_NUM = 10
    SIZE = size
    n = n


    sieve = [i for i in range(SIZE)]
    sieve[1] = 0

    for i in range(2, SIZE):
        if sieve[i] != 0:
            j = i + i
            while j < SIZE:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    # print(res[n - 1])
    print(res)

# sieve(100, 1)

# les_4_task_2.sieve(100, 25)
# 100 loops, best of 3: 19.2 usec per loop
# 100 loops, best of 3: 20 usec per loop
# 100 loops, best of 3: 19.4 usec per loop

# les_4_task_2.sieve(1000, 100)
# 100 loops, best of 3: 568 usec per loop
# 100 loops, best of 3: 530 usec per loop
# 100 loops, best of 3: 243 usec per loop

# les_4_task_2.sieve(10000, 1000)
# 100 loops, best of 3: 2.83 msec per loop
# 100 loops, best of 3: 2.83 msec per loop
# 100 loops, best of 3: 2.85 msec per loop

# cProfile.run('sieve(100, 25)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:6(sieve)
# cProfile.run('sieve(1000, 100)')
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:6(sieve)
# cProfile.run('sieve(10000, 1000)')
# 1    0.023    0.023    0.025    0.025 les_4_task_2.py:6(sieve)


# Сложность алгоритма близко к O(n**2/3)


def no_sieve(size, n):
    SIZE = size
    res = []
    for i in range(2, SIZE):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)
    # print(res[n - 1])


# les_4_task_2.no_sieve(100, 25)
# 100 loops, best of 3: 73.1 usec per loop
# 100 loops, best of 3: 73.9 usec per loop
# 100 loops, best of 3: 74.2 usec per loop

# les_4_task_2.no_sieve(1000, 100)
# 100 loops, best of 3: 3.92 msec per loop
# 100 loops, best of 3: 3.98 msec per loop
# 100 loops, best of 3: 3.92 msec per loop

# les_4_task_2.no_sieve(10000, 1000)
# 100 loops, best of 3: 381 msec per loop
# 100 loops, best of 3: 374 msec per loop
# 100 loops, best of 3: 371 msec per loop

# cProfile.run('no_sieve(100, 25)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:51(no_sieve)
# cProfile.run('no_sieve(1000, 100)')
# 1    0.011    0.011    0.011    0.011 les_4_task_2.py:51(no_sieve)
# cProfile.run('no_sieve(10000, 1000)')
# 1    0.789    0.789    0.789    0.789 les_4_task_2.py:51(no_sieve)

# Сложность алгоритма O(n**2)


def sieve_2(size, n):
    MAX_NUM = 10
    SIZE = size
    n = n


    sieve = [i for i in range(SIZE)]
    # можно попробовать сократить выкинув все четные числа, но не уверен, что Эратосфен умел делить на цело
    sieve[1] = 0

    for i in range(2, int(sqrt(SIZE))):
        if sieve[i] != 0:
            j = i * i
            while j < SIZE:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    # print(res[n - 1])

# les_4_task_2.sieve_2(100, 25)
# 100 loops, best of 3: 12.7 usec per loop
# 100 loops, best of 3: 12.6 usec per loop
# 100 loops, best of 3: 12.5 usec per loop

# les_4_task_2.sieve_2(1000, 100)
# 100 loops, best of 3: 152 usec per loop
# 100 loops, best of 3: 153 usec per loop
# 100 loops, best of 3: 164 usec per loop

# les_4_task_2.sieve_2(10000, 1000)
# 100 loops, best of 3: 1.84 msec per loop
# 100 loops, best of 3: 1.84 msec per loop
# 100 loops, best of 3: 1.85 msec per loop

# cProfile.run('sieve_2(100, 25)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:92(sieve_2)
# cProfile.run('sieve_2(1000, 100)')
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:92(sieve_2)
# cProfile.run('sieve_2(10000, 1000)')
# 1    0.004    0.004    0.005    0.005 les_4_task_2.py:92(sieve_2)


# сложность алгоритма O(n * sqrt(n))

#Вывод:
# Самым эффективным методом является sieve_2 т.к. сильно сократил кол-во итераций цикла за счет теории простых чисел.