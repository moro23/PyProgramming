class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

#an = PartyAnimal()
#an.party()
#an.party()
#an.party()
#PartyAnimal.party(an)

### Classes as types

an = PartyAnimal()
#print(f"Type {type(an)}")
#print(f"Type {dir(an)}")
#print(f"Type {type(an.x)}")
#print(f"Type {type(an.party)}")

### Object lifecycle
class PartyAnimal:
    x = 0
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far ', self.x)

    def __del__(self):
        print('I am destructed', self.x)

#an = PartyAnimal()
#an.party()
#an = 42

### Creating Multiple Instances
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

#s.party()
#j.party()

### Inheritance 
""" 
Inheritance refers is a feature of object-oriented programming that allows us to create a new class by extending an existing class
The original class is refered to as the parent class and the new class is referred to as the child class.
"""

## from party import PartyAnimal
class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal('Sally')
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))