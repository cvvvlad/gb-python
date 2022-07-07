# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = []
counter = 1

print("Введите элементы списка и нажмите [Enter] 2 раза чтобы завершить ввод.")
while True:
    input_str = input(f"{counter}-й элемент:\n")
    if not input_str:
        break

    my_list.append(input_str)
    counter += 1

print(f'Начальный массив:{my_list}')

sorted_list = []
for i in range(len(my_list)):
    if i % 2:
        sorted_list.append(my_list[i])
        sorted_list.append(my_list[i-1])
    elif i == len(my_list)-1:
        sorted_list.append(my_list[i])

print(f"Результат:{sorted_list}")
