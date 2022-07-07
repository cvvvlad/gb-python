def capitalize(input_string=''):
    result = ''
    parts = input_string.split(' ')
    for part in parts:
        result += part[0].capitalize()+part[1:]+' '
    return result

print(capitalize("привет мир"))
