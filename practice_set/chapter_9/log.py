word = "python"

with open("log.txt") as f:
    content = f.read()

if (word in content):
    print("word is available")
else:
    print("word is not available")