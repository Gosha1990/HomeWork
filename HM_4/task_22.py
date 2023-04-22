# Задача 22: Даны два неупорядоченных
# набора целых чисел (может быть,
# с повторениями). Выдать без повторений
# в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы
# множеств.
import random

first_set_length = [random.randint(1,10)
                    for _ in range(int(input('Вводим певое число: ')))]
second_set_length =[random.randint(1,10)
                    for _ in range(int(input('Вводим второе чило: ')))]
print(f'Первое множество {first_set_length} \nвторое множество {second_set_length}')
first_set = set(first_set_length)
second_set = set(second_set_length)
ordered_set_1 = sorted(first_set)
ordered_set_2 = sorted(second_set)

print(f'{ordered_set_1}  \n{ordered_set_2}')