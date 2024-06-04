from logger import input_data, print_data

def interface():
    print("Привет! Это телефонный справочник. \n 1 - Запись данных \n 2 - Вывод данных")
    command = int(input('Введите номер нужной операции:'))

    while command != 1 and command != 2:
        print("Введите 1 или 2")
        command = int(input('Введите номер нужной операции: '))

    if command == 1:
        input_data()
    if command == 2:
        print_data()