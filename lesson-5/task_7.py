# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open('text/task7.txt', 'r', encoding='utf-8') as file_obj:
    lines = file_obj.readlines()

firms = []
for line in lines:
    parts = line.split(' ')
    firm = {
        "name": parts[0],
        "form": parts[1],
        "revenue": float(parts[2]),
        "costs": float(parts[3])
    }
    firm["profit"] = firm["revenue"] - firm["costs"]
    firms.append(firm)

result_list = [
    {firm["name"]: firm["profit"] for firm in firms},
    {"average_profit": sum([firm["profit"] for firm in firms if firm["profit"]]) / len(firms)}
]
print(result_list)

with open("text/task7_json.txt", 'w', encoding='utf-8') as file_obj:
    json.dump(result_list, file_obj, ensure_ascii=False)
