# 1. Открывать файл (режим txt)
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# path = 'contact.txt'
# data = open(path, 'w')
# for line in data:
#     print(line)
# data.close()

def open_file_read(path):
    '''Функуия считыает данные из файла тхт'''
    with open(path,'r') as file:
        main_list=(file.readlines())
        main_list_str=[x.rstrip().split(':') for x in main_list]
    return main_list_str

print(open_file_read('contact.txt'))

def open_file_write(path, list_file):
    '''Функция вносит изменения в файл тхт'''
    with open(path, 'w') as file:
        file.writelines([':'.join(x)+'\n' for x in list_file])
# list_for_look=[['Prohor', '89234567436', 'coment'], ['Boris', '89234542312', 'coment'], ['Klava', '89834535445', 'Coment'], ['sadrgf', 'sdfg', 'dfg'], ['sgdsf', 'sdfg', 'sgdf']]
def look_list (list_for_look):
    print([' '.join(x) for x in list_for_look], end='\n')

# look_list(list_for_look)