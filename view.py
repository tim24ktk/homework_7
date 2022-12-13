from datetime import datetime as dt


def select_action():
    print('''Выберите действие:
            1: запись контакта
            2: поиск контакта''')
    return int(input('-> '))


def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    time = dt.now().strftime('%H:%M')

    return {'surname': surname, 'name': name, 'phone_number': phone_number, 'time': time}


def search_contact():
    return input('Введите данные контакта: ')