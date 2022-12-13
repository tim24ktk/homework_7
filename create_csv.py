import csv


def create_csv(data):
    with open('log.csv', 'a', newline='', encoding='utf-8') as file:
        names = ['surname', 'name', 'phone_number', 'time']
        file_writer = csv.DictWriter(file, delimiter=",", lineterminator="\r", fieldnames=names)

        if file.tell() == 0:
            file_writer.writeheader()

        file_writer.writerow(data)
