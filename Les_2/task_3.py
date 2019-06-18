# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

n = int(input('Введите кол-во чисел: '))
summ = 0
max_num = 0

for i in range(n):
    number = int(input('Введите число: '))
    num = number
    s = 0
    while True:
        s += num % 10
        if num < 10:
            if s > summ:
                summ = s
                max_num = number
            break
        num = num // 10

print(f'Сумма = {summ}, у числа {max_num}')