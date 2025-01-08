class OvverrideLenMethod:

    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    

array = OvverrideLenMethod([1,2,4,6])
print(len(array))