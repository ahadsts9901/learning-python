class MyClass:
    a = 89

    @classmethod
    def get_number(cls):
        print(f"number is {cls.a}")


new_class = MyClass()
new_class.get_number()
new_class.a = 56
new_class.get_number()
