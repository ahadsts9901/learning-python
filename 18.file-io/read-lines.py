# f = open("main.txt")
# lines = f.readlines()
# print(lines,type(lines))
# f.close()


file = open("main.txt")

# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)
# line3 = file.readline()
# print(line3)
# line4 = file.readline()
# print(line4)
# line5 = file.readline()
# print(line5)
# line6 = file.readline()
# print(line6 == "")
line = file.readline()
while(line != ""):
    print(line)
    line = file.readline()

file.close()
