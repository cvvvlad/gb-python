class DivideByZeroError(Exception):
    pass


def divide(a, b):
    if b == 0:
        raise DivideByZeroError("На ноль делить нельзя!")
    if b == 2:
        raise ArithmeticError("На 2 делить не дам!")
    return a / b


nums = [
    (6, 3),
    (25, 4),
    (13, 7),
    (1024, 2),
    (325, 0)
]

for a, b in nums:
    try:
        print(f"{a}/{b}={divide(a, b):.2f}")
    except DivideByZeroError as err:
        print(f"Не могу разделить {a} на {b}. {err}")
    except Exception as err:
        print(f"Непредвиденная ошибка при делении {a} на {b}. {err}")
    else:
        print("прошло успешно!")
    finally:
        print("The End\n")
