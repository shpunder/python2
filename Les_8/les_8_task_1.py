# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.


def counter(msg):
    result = set()

    for i in range(len(msg)):
        for j in range(i + 1, len(msg) + 1):
            if j == len(msg) and i == 0:
                break
            result.add(hash(msg[i:j]))

    return len(result)

    
msg = input("Введите строку S: ")
print(f'Количество уникальных слов = {counter(msg)}') 

print('Проверим работу:')
if counter('papa') == 6:
    print('ОК')

if counter('sova') == 9:
    print('ОК')

