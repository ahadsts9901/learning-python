class MyClass:
    a = 0

o = MyClass()
print(o.a) # print the class attribute because instance attribute is not set
o.a = 6 # set the instance attribute
print(o.a) # print the instance attribute because it is present now
print(MyClass.a) # print the class attribute
