# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке


# def rifma(words):
#     words = words.lower().split()
#     return sum(1 for i in words if i in 'аеёиоуыэюя')
# tranquility = input('Введите стихотворение: ')
# print(rifma(tranquility))
def rifma(word):
    strk = word.split()
    list_1 = []
    for word in strk:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_1.append(sum_w)
    return len(list_1) == list_1.count(list_1[0])
str_1 = input('Введите стихотворение: ')
if rifma(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
