# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['Vasiliy', 13.2, 23, True, {'name': 'Nikolay', 'age': 32}, (1, 2), [3, 4]]

type_names = {
    str: 'строка',
    float: 'число с плавающей точкой',
    int: 'целое число',
    dict: 'словарь',
    bool: 'логический',
    tuple: 'кортеж',
    list: 'список'
}


for i in range(len(my_list)):
    item = my_list[i]
    item_type = type(item)
    item_type_name = type_names[item_type]
    print(f"тип {i}-го элемента ({item}) - {item_type_name} ({item_type})")
