class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {
        "wage": 0,
        "bonus": 0
    }


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


positions = [
    Position("Николай", "Жданов", "Водитель", 15000, 5500),
    Position("Иван", "Носков", "Бухгалтер", 35000, 4200),
    Position("Игорь", "Купцов", "Ветеринар", 32000, 8600)
]

for position in positions:
    print(f"{position.get_full_name()} Должность:{position.position} Доход:{position.get_total_income()}")
