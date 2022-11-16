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
print(f"Type {type(an)}")
print(f"Type {dir(an)}")
print(f"Type {type(an.x)}")
print(f"Type {type(an.party)}")