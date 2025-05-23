class Dog:
    def __init__(self,name,breed,location):
        self.name=name
        self.breed=breed
        self.location=location
        self.trick=[]

    def bark(self):
        print(f"{self.name} says Boo Boo!")

    def learn_trick(self,new_trick):
        if new_trick not in self.trick:
            self.trick.append(new_trick)


nomi=Dog("Nomi","Laba","Pune")
Rita=Dog("Rita","CHota","Mumbai")

# nomi.bark()
# Rita.bark()

nomi.learn_trick("sleep")
nomi.learn_trick("slBarkeep")
nomi.learn_trick("sleep")
Rita.learn_trick("sit")
Rita.learn_trick("walk")
Rita.learn_trick("walk")

print(nomi.trick)
print(Rita.trick)