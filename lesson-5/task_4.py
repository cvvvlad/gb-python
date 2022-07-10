# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from translate import Translator

translator = Translator(to_lang="Russian")

with open("text/task4_in.txt", 'r', encoding='utf-8') as file_obj:
    lines = file_obj.readlines()

translated_lines = []
for line in lines:
    parts = [part.strip() for part in line.split("-")]
    word = parts[0]
    rus_word = translator.translate(word)
    translated_lines.append(line.replace(word, rus_word))

with open("text/task4_out.txt", 'w', encoding='utf-8') as file_obj:
    file_obj.writelines(translated_lines)
