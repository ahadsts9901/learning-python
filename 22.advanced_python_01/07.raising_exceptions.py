a = int(input("enter first number: "))
b = int(input("enter second number: "))

if (b == 0) :
    raise ZeroDivisionError("hey zero is not allowed")
else:
    print(f"the division is {a/b}")

    