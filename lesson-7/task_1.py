class Matrix:

    def __init__(self, input_rows):
        self.rows = input_rows
        self.rows_count = len(self.rows)
        self.columns_count = len(self.rows[0])

    def __str__(self):
        result_string = ""
        for row in self.rows:
            result_string += " ".join([str(el) for el in row])
            result_string += "\n"
        return result_string

    def __add__(self, other):
        if self.rows_count != other.rows_count or self.columns_count != other.columns_count:
            raise ArithmeticError("Нельзя складывать матрицы разных размерностей!")
        result_rows = []
        for row_num in range(self.rows_count):
            new_row = []
            for el_num in range(self.columns_count):
                new_row.append(self.rows[row_num][el_num] + other.rows[row_num][el_num])
            result_rows.append(new_row)
        return Matrix(result_rows)


matrix1 = Matrix([[1, 2, 3],
                  [4, 5, 6]])

matrix2 = Matrix([[2, 3, 4],
                  [5, 6, 7]])

print(matrix1 + matrix2)
