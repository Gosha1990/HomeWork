#  На столе лежат n монеток.
# Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите
# минимальное число монеток, которые
# нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет,
# которые нужно перевернуть
import random

n = int(input('Введем количество монет: '))
count_tails = 0
count_erne = 0
for i in range(n):
    x = random.randint(0, 1)
    print(x, end= " ")
    if x == 0:
        count_tails += 1
    else:
        count_erne +=1
if count_tails  < count_erne:
        print(f'\nМинимальное количествоcoun {count_tails} ')
elif count_tails == count_erne:
    print('\nОдинаково монет нужно перевернуть ')
else:
    print(f'\nМинимальное количество {count_erne} ')
