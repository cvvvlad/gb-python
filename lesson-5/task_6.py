# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re

with open("text/task6.txt", 'r', encoding='utf-8') as file_obj:
    lines = file_obj.readlines()

subjects = []
for line in lines:
    subject = {
        "name": line[:line.find(':')],
        "lectures": []
    }
    matches = re.findall(r"(\d+)\(([а-яА-Я]+)\)", line)
    for m_count, m_type in matches:
        subject["lectures"].append({
            "type": m_type,
            "count": int(m_count)
        })
    subjects.append(subject)

result_dict = {el["name"]: sum([lect["count"] for lect in el["lectures"]]) for el in subjects}
print(result_dict)
