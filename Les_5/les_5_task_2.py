# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import Counter

def make_arr(num):
    arr = []
    for item in num:
        if item == 'A':
            arr.append(10)
        elif item == 'B':
            arr.append(11)
        elif item == 'C':
            arr.append(12)
        elif item == 'D':
            arr.append(13)
        elif item == 'E':
            arr.append(14)
        elif item == 'F':
            arr.append(15)
        else:
            arr.append(int(item))
    return arr

def make_number(num):
    result = ''
    for item in num[::-1]:
        if item == 10:
            result += 'A'
        elif item == 11:
            result += 'B'
        elif item == 12:
            result += 'C'
        elif item == 13:
            result += 'D'
        elif item == 14:
            result += 'E'
        elif item == 15:
            result += 'F'
        else:
            result += str(item)
    return result




number = input('Введите первое число: ')
counter = Counter(number)
counter = list(counter.elements())
a = make_arr(counter)

number = input('Введите второе число: ')
counter = Counter(number)
counter = list(counter.elements())
b = make_arr(counter)

if len(a) > len(b):
    a, b = b, a

def summ(a, b):

    k = 0
    result = []
    for i, item in enumerate(b[::-1]):
        if i < len(a):
            r = item + a[-(i + 1)] + k
        else:
            r = item + k
        if r > 15:
            result.append(r % 16)
            k = 1
        else:
            result.append(r)
            k = 0
    if k:
        result.append(k)

    return result[::-1]

print('Сложили: ', make_number(summ(a, b)))

# умножение
k = 0
result = []
res2 = []
for item in b[::-1]:
    res = []
    for j in a[::-1]:
        r = item * j + k
        if r > 15:
            res.append(r % 16)
            k = r // 16
        else:
            res.append(r)
            k = 0
    if k:
        res.append(k)
        k = 0
    res2.append(res[::-1])

# сложим все элементы
result = res2.pop()
result.insert(0, 0)
for item in range(len(res2)):
    one = res2.pop()
    for i in range(item + 1):
        one.append(0)

    result = summ(result, one )
    if result[0] == 0:
        result.pop(0)
    

print('Умножили: ', make_number(result[::-1]))
