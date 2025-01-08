class Calculator:
    def __init__(self, num) :
        self.num = num

    def get_square_root(self) :
        print(f"square root of {self.num} is: {self.num ** 1/2}")
    
    def get_square(self) :
        print(f"square of {self.num} is: {self.num * self.num}")

    def get_cube(self):
        print(f"cube of {self.num} is: {self.num * self.num * self.num}")

num_1 = Calculator(2)
num_1.get_square_root()
num_1.get_square()
num_1.get_cube()

num_2 = Calculator(4)
num_2.get_square_root()
num_2.get_square()
num_2.get_cube()