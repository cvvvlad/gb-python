a = float(input('Результат в 1-й день (км):'))
b = float(input('Цель (км):'))

day = 1
day_result = a
while day_result < b:
    day = day + 1
    day_result = day_result + (day_result/100)*10
    print(f'День {day}: {day_result:.1f} км')

print(f'Ответ: на {day} день спортсмен достиг результата не менее {b} км')