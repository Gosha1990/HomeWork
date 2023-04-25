# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень
# B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def number_to_the_power(num, exp):
    if (exp == 1):
        return (num)
    if (exp != 1):
        return (num * number_to_the_power(num, exp - 1))
num = int(input('Вводим возводимое число: '))
exp = int(input('Вводим чило являющееся степенью: '))
print(f'Резултат равен {number_to_the_power(num, exp)}')