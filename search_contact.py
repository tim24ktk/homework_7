import csv


def search_contact(value):
    result = ''
    with open('log.csv', encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=',')

        for row in file_reader:
            if value in row.values():
                for key, value in row.items():
                    result += f'{key}: {value}\n'

    if result:
        return result
    else:
        return 'По вашему запросу нет результата!'

