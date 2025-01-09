try:
    with open("1.txt") as f:
        f.read()
except Exception as e:
    print(e)

try:
    with open("2.txt") as f:
        f.read()
except Exception as e:
    print(e)

try:
    with open("3.txt") as f:
        f.read()
except Exception as e:
    print(e)


print("thank you")