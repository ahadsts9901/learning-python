class SecurityGuard:
    name = ""

    def __init__(self,name):
        self.name = name

    def get_power(self):
        print(f"{self.name} is so powerful")


class Coder:
    name = ""

    def __init__(self,name):
        self.name = name

    def get_intellisense(self):
        print(f"{self.name} is so intellogent")



class Officer(SecurityGuard, Coder):
    name = ""

    def __init__(self,name):
        self.name = name





security_guard = SecurityGuard("Pakhtawar")
security_guard.get_power()

coder = Coder("Saim")
coder.get_intellisense()

officer = Officer("Basit")
officer.get_intellisense()
officer.get_power()