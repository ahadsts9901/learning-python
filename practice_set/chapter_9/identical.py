with open("identical1.txt") as f:
    contant_1 = f.read()


with open("identical2.txt") as f:
    contant_2 = f.read()

if(contant_1 == contant_2):
    print("matched")
else:
    print("not_matched")