# Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


# В файле task2.txt сгенерирован текст на 50 слов через сервис https://ru.lipsum.com
# также добавил туда два слова и много лишних пробелов и переводов строк для теста
with open('text/task2.txt', 'r', encoding='utf-8') as file_obj:
    lines = file_obj.readlines()

lines_count = len(lines)
all_words_count = 0
for line in lines:
    words = [word for word in line.split(" ") if word and word != '\n']
    print(words)
    words_count = len(words)
    all_words_count += words_count

print(f"Файл:{file_obj.name} Строык:{lines_count} Слов:{all_words_count}")
