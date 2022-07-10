# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
import random

# write
with open("text/task5.txt", 'w', encoding='utf-8') as file_obj:
    file_obj.write(' '.join([str(random.randint(-100, 100)) for i in range(0, 100)]))

# read
with open("text/task5.txt", 'r', encoding='utf-8') as file_obj:
    numbers = [int(part.strip()) for part in file_obj.readline().split(' ')]
    print(sum(numbers))
