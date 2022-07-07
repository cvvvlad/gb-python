revenue = float(input("Выручка:"))
expenses = float(input("Издержки:"))

#финансовый результат
is_profit = revenue > expenses

print('Финансовый результат:' 'Прибыль' if is_profit else 'Убыток')

if not is_profit: exit()

profit = revenue - expenses
profitability = profit / revenue
print(f'Прибыль:{profit:.2f}')
print(f'Рентабельность выручки:{profitability:.2f}')

employees_count = int(input("Кол-во сотрудников фирмы:"))

profit_per_employee = profit / employees_count

print(f'Прибыль фирмы в расчёте на одного сотрудника: {profit_per_employee:.2f}')
