# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict

seasons = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

while True:
    input_month = input("Введите номер месяца:")
    if not input_month or not input_month.isdigit() or int(input_month) < 1 or int(input_month) > 12:
        print("Не верный ввод. Введите число от 1 до 12")
    else:
        break
input_month = int(input_month)

result_season_name = ''
for season_name in seasons:
    for month_number in seasons[season_name]:
        if month_number == input_month:
            result_season_name = season_name

print(f"\n{input_month}-й месяц это {result_season_name}")
