# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

def greater_only_gen(input_list):
    for item in input_list:
        index = input_list.index(item)
        if index == 0:
            continue
        prev_el = input_list[index - 1]
        if item > prev_el:
            yield item


input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for el in greater_only_gen(input_list)]

print(result_list)
