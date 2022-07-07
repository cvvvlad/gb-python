def my_func(x, y):
    result = x
    for i in range(y-1):
        result *= x
    return result


print(my_func(2, 6))
