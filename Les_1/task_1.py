# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input('Введите трехзначное число: '))

n1 = n % 10
n = n // 10
n2 = n % 10
n = n // 10

print(f'Сумма чисел = {n + n1 + n2}')
print(f'Произведение чисел = {n * n1 * n2}')
