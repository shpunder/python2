# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
import random

count =  int(input('Введите кол-во организаций '))


Company = namedtuple('Company', ['c1', 'c2', 'c3', 'c4'])

companies = {}

for i in range(count):
    name = 'Компания ' + str(i)
    c1 = int(input('Перрвый квартал '))
    c2 = int(input('Второй квартал '))
    c3 = int(input('Третий квартал '))
    c4 = int(input('Четвертый квартал '))

    companies[name] = Company(
        c1=c1,
        c2=c2,
        c3=c3,
        c4=c4
    )

total_sum = 0
for item, arr in companies.items():
    for s in arr:
        total_sum += s

avg = total_sum / count / 4
print(f'Среднее = {avg}')


over = []
less = []

for item, arr in companies.items():
    summ = 0
    for s in arr:
        summ += s
    if summ / 4 > avg:
        over.append(item)
    else:
        less.append(item)

for item in over:
    print(f'Больше {item}')

for item in less:
    print(f'Меньше или равно {item}')

