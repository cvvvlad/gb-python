from math import ceil


class Cell:

    def __init__(self, size):
        self.size = int(size)

    def __str__(self):
        return f"Клетка({self.size} ячеек)"

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        diff = self.size - other.size
        if diff > 0:
            return Cell(diff)
        else:
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def make_order(self, columns):
        return (("*" * columns) + "\n") * ceil(self.size / columns)

    def print_ordered(self, columns):
        print(f"{self} по {columns} ячеек в ряду:")
        print(self.make_order(columns))


cell_1 = Cell(12)
cell_2 = Cell(4)
print(f"{cell_1} + {cell_2} = {cell_1 + cell_2}")
print(f"{cell_1} - {cell_2} = {cell_1 - cell_2}")
print(f"{cell_1} * {cell_2} = {cell_1 * cell_2}")
print(f"{cell_1} / {cell_2} = {cell_1 / cell_2}")

print(f"{cell_2} - {cell_1} = {cell_2 - cell_1}")

cell_1.print_ordered(5)
cell_1.print_ordered(6)
cell_2.print_ordered(12)
cell_2.print_ordered(3)
