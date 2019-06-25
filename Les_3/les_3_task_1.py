# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

# SIZE = 97
MIN_ITEM = 2
MAX_ITEM = 99
MAX_DIGIT = 9
array = [i for i in range(MIN_ITEM, MAX_ITEM + 1)] 
result = {d: 0 for d in range(MIN_ITEM, MAX_DIGIT + 1)}

for item in array:
    for d in result:
        if item % d == 0:
            result[d] += 1

print(result)



