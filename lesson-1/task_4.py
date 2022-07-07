input_str = input('Введите число:')

max = 0
i = 0
while i < len(input_str):
    digit = int(input_str[i])
    if digit > max:
        max = digit
    i = i+1

print(f'Максимальная цифра в числе {input_str} - {max}')