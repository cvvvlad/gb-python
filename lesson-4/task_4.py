# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
import random


# генератор уникальных записей
def distinct_gen(input_list):
    used_items = set()
    for el in input_list:
        if el not in used_items:
            used_items.add(el)
            yield el


# генератор случайных чисел, сделал для эксперимента над большим объемом данных в разном порядке
def random_range_gen(limit):
    uniq_items = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    for i in range(limit):
        yield random.choice(uniq_items)


# input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]*10000
input_list = [el for el in random_range_gen(100000)]
result_list = [el for el in distinct_gen(input_list)]

print(input_list)
print(result_list)
