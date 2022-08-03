class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __str__(self):
        real = f"{self.real}" if self.real else ''
        imag = f"{self.imag}" if self.imag > 1 or self.imag < -1 else ''
        sign = "+" if real and imag and self.imag > 0 else ''
        sign = "-" if self.imag == -1 else sign
        i = "i" if self.imag else ''

        return f"{real}{sign}{imag}{i}"


def print_add(a: Complex, b: Complex):
    print(f"({a}) + ({b}) = {a + b}")


def print_mul(a: Complex, b: Complex):
    print(f"({a}) * ({b}) = {a * b}")


c1 = Complex(2, 5)
print(c1)

c2 = Complex(-3, -6)
print(c2)

c3 = Complex(0, 2)
print(c3)

c3 = Complex(-4, 0)
print(c3)

print_add(c1, c2)
print_mul(c2, c3)

res = c1 + c2

print(res)
