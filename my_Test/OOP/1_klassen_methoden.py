class CAJLAKOVIC():
    def get_name(self): # Methode ist eine Funktion die sich auf eine classe bezieht! => OOP
        print(self.firstName + " " + self.lastName + ": " + self.age)


son = CAJLAKOVIC()  # son oder daughter ist eine Instanz für die nachfolgende eigenschaft
son.firstName = "Adis"  # .firstName oder .lastName sind eigenschaften!
son.lastName = "Cajlakovic"
son.age = "4"
son.get_name() # hiermit rufe ich eine Methode auf oder eine funktion in einer classe

daughter = CAJLAKOVIC()
daughter.firstName = "Emma"
daughter.lastName = "Cajlakovic"
daughter.age = "0"
daughter.get_name()

mama = CAJLAKOVIC()
mama.firstName = "Enida"
mama.lastName = "Cajlakovic"
mama.age = "35"
mama.get_name()

babo = CAJLAKOVIC()
babo.firstName = "Elvedin"
babo.lastName = "Cajlakovic"
babo.age = "34"
babo.get_name()
