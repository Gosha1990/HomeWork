class Phonebook:

    def __init__(self, path: str = 'phonebook.txt'):
        self._phone_book: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0

    '''Открыть телефонную книгу'''

    def open_pb(self):
        with open(self._path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]}
            self._phone_book.append(new)

    '''Сохранение контакта'''

    def save_pb9(self):
        data = []
        for contact in self._phone_book:
            data.append(':'.join([value for value in contact.values()]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write(data)

    '''Показать контакт'''

    def get_pb(self):
        return self._phone_book

    '''Добавление контакта'''

    def add_contact(self, new: dict[str, str]) -> str:
        self._last_id += 1
        new['id'] = str(self._last_id)
        self._phone_book.append(new)
        return new.get('new')

    '''Поиск контакта'''

    def search_contact(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for contact in self._phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result

    '''Замена контакта'''

    def change_contact(self, new: dict, index: int):
        for contact in self._phone_book:
            if index == contact.get('id'):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comment'] = new.get('comment', contact.get('comment'))
                return contact.get('name')

    '''Удаление контакта'''

    def delet_contakt(self, index: int) -> str:
        del_con = self._phone_book.pop(index - 1)
        return del_con.get('name')
