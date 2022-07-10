# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    last_value = 1
    if n == 0:
        yield 1

    if n < 0:
        raise ArithmeticError("Факториал можно определить только для не отрицательного целого числа")

    for i in range(1, n + 1):
        last_value *= i
        yield last_value


def print_fact(n):
    fact_list = [str(el) for el in fact(n)]
    fact_result = fact_list[len(fact_list) - 1]
    fact_list_str = [f"{fact_list[i]} * {i + 2}" for i in range(0, len(fact_list) - 1)]
    print(f"{n}! = {' => '.join(fact_list_str)} = {fact_result}")


print_fact(10)
