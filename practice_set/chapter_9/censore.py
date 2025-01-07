words = ["donkey", "bad", "ganda"]

with open("censore.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("censore.txt","w") as n:
    n.write(content)