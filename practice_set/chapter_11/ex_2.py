class Animal:
    pass


class Pet(Animal):
    pass

class Dog(Pet):

    @staticmethod
    def bark():
        print("Bow bow!")


dog = Dog()
dog.bark()