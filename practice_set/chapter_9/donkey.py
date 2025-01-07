with open("donkey.txt", "r") as f:
    content = f.read()

new_str = content.replace("donkey", "######")

with open("donkey.txt","w") as n:
    n.write(new_str)