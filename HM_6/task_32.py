# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

print(list_1 := [random.randint(-15, 15) for _ in range(15)])
min_num = int(input('Вводим нижнюю границу'))
max_num = int(input('Вводим верхнюю границу'))
for i in range(len(list_1)):
    if min_num <= list_1[i] <= max_num:
        print(i , end=',')

