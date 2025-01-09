a = int(input("enter first number: "))
b = int(input("enter second number: "))

try:
    print(f"division is {a / b}")

except ZeroDivisionError as z:
    print("infinite") 


print("thanks")

