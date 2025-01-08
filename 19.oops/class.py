class Employee:
    salary = "1000000" # class attribute
    language = ["py", "ts", "js"] # class attribute

mani = Employee()

mani.name = "Ahad" # object attribute || instance attribute

print(mani.name, mani.salary, mani.language)


# here name is object attribute and salary & languuage are class attribute as they directly belongs to the class