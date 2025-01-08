class Calculator:
    def __init__(self, num) :
        self.num = num

    def get_square_root(self) :
        print(f"square root of {self.num} is: {self.num ** 1/2}")
    
    def get_square(self) :
        print(f"square of {self.num} is: {self.num * self.num}")

    def get_cube(self):
        print(f"cube of {self.num} is: {self.num * self.num * self.num}")

    @staticmethod
    def greet():
        print("hello world")


num_1 = Calculator(3)
num_1.greet()