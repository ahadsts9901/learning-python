from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"train no {self.trainNo} booked from {fro} to {to}")

    def getStatus(self):
        print(f"train {self.trainNo} is on the way")
    
    def get_fare(self, fro, to):
        print(f"fare in train {self.trainNo} from {fro} to {to} is {randint(1200,1500)}")

train_1 = Train(1849)

train_1.book("Karachi", "Sukkur")
train_1.getStatus()
train_1.get_fare("Karachi", "Sukkur")