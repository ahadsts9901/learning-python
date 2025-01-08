class Employee:
    salary = 1200000
    language = "python"

    def __init__(self, name, salary, language): # ====> dunder method whick is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("i am getting an object")

    def getInfo(self):
        print(f"slary is {self.salary} and language is {self.language}")

    @staticmethod
    def greet():
        print("hello world")

saim = Employee("saim", 1400000, "javascript")

print(saim.name, saim.salary, saim.language)