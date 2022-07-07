def my_func(param_1, param_2, param_3):
    params = [param_1, param_2, param_3]
    result = 0
    min_value = min(params)
    for param in params:
        if param == min_value:
            continue
        result += param
    return result


print(my_func(3, -2, -1))
