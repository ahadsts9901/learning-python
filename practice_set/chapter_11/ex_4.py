class Complex:

    def __init__(self, num):
        self.num = num

    def __add__(self, val):
        return self.num + val.num
    
    def __sub__(self, val):
        return self.num - val.num

    def __mul__(self, val):
        return self.num * val.num

    def __add__(self, val):
        return self.num + val.num


num1 = Complex(6)
num2 = Complex(4)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)

