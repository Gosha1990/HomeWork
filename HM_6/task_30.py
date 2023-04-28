#   Заполните массив элементами арифметической прогрессии.
#   Её первый элемент, разность и количество
#   элементов нужно ввести с клавиатуры.
#   Формула для получения n-го члена прогрессии:
#   an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
import random

list_length = int(input("Вводим длину списка: "))
list_step = int(input("Вводим шаг: "))
beginning_of_the_list = int(input("Вводим число с которого начнется список: "))
for i in range(list_length):
    print(beginning_of_the_list + i * list_step, end=' ')