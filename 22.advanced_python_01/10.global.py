a = 56

def fun():
    global a 
    a = 89
    print(a)

fun()
print(a)