class Employee:
    language = "javascript",
    salary = 1200000
    def get_info(self):
        print(f"salary is {self.salary} and language is {self.language}")
    

    @staticmethod
    def greet():
        print("hello world")

user = Employee()

user.get_info() # same behaviour
Employee.get_info(user) # same behaviour

user.greet()