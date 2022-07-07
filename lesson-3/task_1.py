def divide(x, y):
    if y == 0:
        raise ArithmeticError("Делить на ноль нельзя!")
    return x/y


divide(3, 0)
