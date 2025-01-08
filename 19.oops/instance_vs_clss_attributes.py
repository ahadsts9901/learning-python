class Employee:
    language = "javascript"
    salary = 1500000

user = Employee()

user.language = "python"

print(user.language, user.salary)