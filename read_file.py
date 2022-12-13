def read_file():
    with open('log.csv', 'r') as file:
        values = file.read().split('\n')

    return values
