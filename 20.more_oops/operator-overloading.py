class Number:

    def __init__(self,n):
        self.n = n

    def __add__(self,value):
        return self.n + value.n
    
    def __mul__(self, value):
        return self.n * value.n
    
    def __sub__(self, value):
        return self.n - value.n
    
    def __len__(self,value):
        return

number1 = Number(1)
number2 = Number(2)

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)