def parse_and_sum(input_string, exit_char = ';'):
    parts = input_str.split(' ')
    sum_of_parts = 0
    exit_char_exists = False
    for part in parts:
        if part == exit_char:
            exit_char_exists = True
            break
        num = int(part)
        sum_of_parts += num
    return sum_of_parts, exit_char_exists


all_sum = 0
while True:
    input_str = input("Введите числа разделённые пробелом:")
    result = parse_and_sum(input_str)
    all_sum += result[0]
    need_to_exit = result[1]
    print(f"Сумма:{all_sum}")
    if need_to_exit:
        break
