class OnlyNumbersError(Exception):

    def __init__(self, input_string, msg):
        self.input_string = input_string
        super().__init__(msg)

def is_num(cls, str):
    try:
        cls(str)
        return True
    except ValueError:
        return False


def get_input_num():
    input_str = input("Введите число:").replace(',', '.')
    is_int = is_num(int, input_str)
    is_float = is_num(float, input_str)
    if not (is_float or is_int):
        raise OnlyNumbersError(input_str, "Вводить можно только числа!")
    return int(input_str) if is_int else float(input_str)


input_numbers = []

while True:
    try:
        input_numbers.append(get_input_num())
    except OnlyNumbersError as err:
        if err.input_string == 'stop':
            print(input_numbers)
            break
        else:
            print(err)
