class SecurityGuard:
    
    def __init__(self):
        print("security guard constructor")


class Coder(SecurityGuard):
    
    def __init__(self):
        super().__init__()
        print("coder constructor")



class Officer(Coder):

    def __init__(self):
        super().__init__()
        print("officer constructor")


security_guard = SecurityGuard()
coder = Coder()
officer = Officer()
