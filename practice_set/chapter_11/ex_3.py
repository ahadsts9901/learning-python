class Employee:

    salary = 80000
    increment = 25

    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * (self.increment / 100)))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val):
        self.increment = (val - self.salary)


e = Employee()

print(e.salary)
print(e.increment)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 120000
print(e.increment)

