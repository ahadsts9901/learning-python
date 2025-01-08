class Programmer:
    company = "microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @staticmethod
    def greet():
        print("hello company")


new_programmer = Programmer("mani", 1800000)

print(new_programmer.company, new_programmer.name, new_programmer.salary)