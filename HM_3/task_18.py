# Задача 18: Требуется найти в массиве
# A[1..N] самый близкий по величине
# элемент к заданному числу X.
# Пользователь в первой строке вводит
# натуральное число N – количество
# элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

N = int(input('вводим размер списка: '))
list_N = [random.randint(0, 10) for i in range(N)]
print(list_N)
X = int(input('Вводим: '))
intimate = list_N.count(X)
min = list_N[0]
if intimate == 0:
    for num in list_N:
        if abs(X - num) < abs(X - intimate):
            intimate = num
print(f'Ближайшее к {X} число {intimate} ')
