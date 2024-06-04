from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате сохранить данные:\n\n"
    f"1 вариант:\n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант:\n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант:"))
    while var != 1 and var != 2:
        print("Введите 1 или 2")
        var = int(input('Введите номер нужной операции: '))
    if var == 1:
        with open('data_1st_var.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open('data_2d_var.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")

def print_data():
    print("Вывод данных в формате столбца: \n")
    with open('data_1st_var.csv', 'r', encoding = 'utf-8') as f:
        data_columns = f.readlines()
        data_columns_list = []
        j = 0
        for i in range(len(data_columns)):
            if data_columns == '\n' or i == len(data_columns) - 1:
                data_columns_list.append(''.join(data_columns[j:i+1]))
                j = i
        print(''.join(data_columns_list))
    print("Вывод данных в формате строки: \n")
    with open('data_2d_var.csv', 'r', encoding = 'utf-8') as f:
        data_rows = f.readlines()
        print(*data_rows)


