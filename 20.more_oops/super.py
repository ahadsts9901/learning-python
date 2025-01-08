class SecurityGuard:
    
    def __init__(self):
        print("security guard constructor")


class Coder(SecurityGuard):
    
    def __init__(self):
        super().__init__() # runs the parent constructor also
        print("coder constructor")



class Officer(Coder):

    def __init__(self):
        super().__init__() # runs the parent constructor also
        print("officer constructor")


security_guard = SecurityGuard()
coder = Coder()
officer = Officer()
