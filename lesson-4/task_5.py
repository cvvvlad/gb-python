# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def even_range_gen(start, stop):
    for i in range(start, stop + 1):
        if i % 2 == 0:
            yield i


my_list = [el for el in even_range_gen(100, 1000)]
print(my_list)

mult_result = reduce(lambda a, b: a * b, my_list)
print(mult_result)
