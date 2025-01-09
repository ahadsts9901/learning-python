with(
    open("abc.txt") as v,
    open("def.txt") as t
) :
    print(v.read())
    print(t.read())

    