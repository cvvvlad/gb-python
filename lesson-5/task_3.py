# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def parse_salaries(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_obj:
        lines = file_obj.readlines()

    salaries = []
    for line in lines:
        parts = line.split(" ")
        if parts[0] and parts[1]:
            salaries.append({
                "last_name": parts[0],
                "salary": float(parts[1])
            })
    return salaries


def format_money(money):
    return f"{money:,.2f}".replace(',', ' ')


def print_salaries(salaries):
    for user in salaries:
        print(f"\t{user['last_name']} ({format_money(user['salary'])} рублей)")


user_salaries = parse_salaries("text/task3.txt")

print(f"Все данные из файла:")
print_salaries(user_salaries)

print(f"\nЗарплата меньше 20 000 у сотрудников:")
print_salaries([user for user in user_salaries if user["salary"] < 20000])

avg_salary = sum([user['salary'] for user in user_salaries]) / len(user_salaries)
print(f"\nСредний доход сотрудников:{format_money(avg_salary)} рублей")
