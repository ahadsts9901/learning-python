# abstraction : implementation details ko hamne chupa dia user sy
# encapsulation : bahut sare kaam krny waly components ko aik unit me pack krdia like "class"
# inheritance : parent se koi cheez inherit krli

class User:

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
        
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


newuser = User()

newuser.name = "Abdul Ahad"

print(newuser.fname)
print(newuser.lname)
print(newuser.name)