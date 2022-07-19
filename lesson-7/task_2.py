from abc import ABC, abstractmethod


class Clothes(ABC):
    name = ''

    @property
    @abstractmethod
    def material_consumption(self):
        raise NotImplemented

    @property
    def material_consumption_str(self):
        return f"Расход ткани: {self.material_consumption:.2f}"


class Coat(Clothes):
    __size = 0.0

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = float(value)

    @property
    def material_consumption(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f"Пальто \"{self.name}\". Размер {self.size}."


class Costume(Clothes):
    __height = 0.0

    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = float(value)

    @property
    def material_consumption(self):
        return 2 * self.height + 0.3

    def __str__(self):
        return f"Костюм \"{self.name}\". Рост: {self.height}."


clothes = [
    Coat('Извозчик', 23),
    Coat('Богатырь', 84),
    Costume("Шпион", 170),
    Costume("Человек-паук", 78)
]

for item in clothes:
    print(f"{item} {item.material_consumption_str}")
