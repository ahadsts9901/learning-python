with open("make_copy.txt") as f:
    content = f.read()

with open("make_copy_copy.txt", "w") as f:
    f.write(content)