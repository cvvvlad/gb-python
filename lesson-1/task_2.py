input_secs = int(input("Введите время в секундах:"))

hours = 0
minutes = 0
seconds = 0

if input_secs >= 60:
    minutes = input_secs // 60
    seconds = input_secs - minutes * 60

if minutes >= 60:
    hours = minutes // 60
    minutes = minutes - hours * 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")