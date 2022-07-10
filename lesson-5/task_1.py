# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open("text/task1.txt", 'w', encoding='utf-8') as file_obj:
    while True:
        input_line = input("Строка:")
        if not input_line:
            break
        file_obj.write(input_line + "\n")
