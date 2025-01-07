word = "python"

with open("line.txt") as f:
    lines = f.readlines()

line_no = 1

for line in lines:
    if (word in line):
        print(f"word is available in line {line_no}")
        break
    line_no += 1

    
else:
    print("word is not available")