# f = open("main.txt")

# data = f.read()
# print(data)

# f.close()

with open("main.txt") as f:
    print(f.read())