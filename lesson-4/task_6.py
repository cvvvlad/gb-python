# Реализовать два небольших скрипта:
#
#     итератор, генерирующий целые числа, начиная с указанного;
#     итератор, повторяющий элементы некоторого списка, определённого заранее.
#     Подсказка: используйте функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Предусмотрите условие его завершения. #### Например, в первом задании выводим целые числа, начиная с 3.
#     При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
#     при котором повторение элементов списка прекратится.

from itertools import count, cycle

# count
count_iter = count(3)
count_iter_list = []
while len(count_iter_list) < 10:
    count_iter_list.append(next(count_iter))
print(count_iter_list)

# cycle
cycle_iter = cycle(count_iter_list)
cycle_iter_list = []
while len(cycle_iter_list) < 40:
    cycle_iter_list.append(next(cycle_iter))
print(cycle_iter_list)
