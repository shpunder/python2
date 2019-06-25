# Найти максимальный элемент среди минимальных элементов столбцов матрицы
import random


SIZE_COL = 3
SIZE_ROW = 5
MIN_ITEM = 1
MAX_ITEM = 99
array = [[random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE_ROW)] for j in range(SIZE_COL)]

for item in array:
    for _ in item:
        print(f'{_:>5}', end='')
    print()

max_ = MIN_ITEM


for i in range(SIZE_ROW):
    min_column = MAX_ITEM
    for j in range(SIZE_COL):
        if min_column > array[j][i]:
            min_column = array[j][i]
    if max_ < min_column:
        max_ = min_column


print(f'Максимальный из минимальных в столбцах = {max_}')









