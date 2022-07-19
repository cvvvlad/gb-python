import re


class InvalidDateError(Exception):
    def __init__(self, date_string, msg):
        self.date_string = date_string
        super().__init__(msg)


class Date:
    day = 0
    month = 0
    year = 0

    def __init__(self, date_string):
        day, month, year = self.parse(date_string)
        if not self.is_valid(day, month, year):
            raise InvalidDateError(date_string, "Не правильная дата.")
        self.day = day
        self.month = month
        self.year = year
        pass

    @classmethod
    def parse(cls, date_string):
        date_match = re.match(r"(\d{2})-(\d{2})-(\d{4})", date_string)
        if not date_match:
            raise InvalidDateError(date_string, f"Не удалось распарсить дату {date_string}")

        return tuple(int(el) for el in date_match.groups())

    @staticmethod
    def is_valid(day, month, year):
        last_day_in_month = 30
        if month in [1, 3, 5, 7, 8, 10, 12]:
            last_day_in_month = 31
        elif month == 2:  # февраль
            is_leap_year = year % 4 == 0  # високосный год?
            last_day_in_month = 29 if is_leap_year else 28
        return year > 0 and 1 <= month <= 12 and 1 <= day <= last_day_in_month

    def __str__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year:04d}"


date_strings = [
    "19-07-2022",
    "28-02-2022",
    "29-02-2020",
    "29-02-2021",
    "01-01-0001",
    "01-01-1",
]

valid_dates = []

for date_str in date_strings:
    is_valid = True
    error_msg = ""
    try:
        date = Date(date_str)
        valid_dates.append(date)
    except InvalidDateError as err:
        is_valid = False
        error_msg = str(err)
    print(f"{date_str} is {('not' if not is_valid else '')} valid. {error_msg}")

print("\nValid dates:")
for valid_date in valid_dates:
    print(valid_date)
