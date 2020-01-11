class Student():

    # dies ist der konstructor!
    def __init__(self, firstName, lastName, age):
        # ----(son etc.,  Adis,  Cajlakovic, 4)

        self.firstName = firstName
        # self ist die instanz einer classe mit der eigenschaft firstName die den wert Adis hat!

        self.lastName = lastName
        # self ist die instanz einer classe mit der eigenschaft lastName die den wert Cajlakovic hat!

        self.age = age
        # self ist die instanz einer classe mit der eigenschaft age die den wert 4 hat!

        # self ist die instanz einer classe mit der eigenschaft semmester die den wert 1 hat!
        self.__semmester = 1

    # nun kann ich den konstruktor um eine weitere funktion(methode) erweitern
    def eingeschriebenes_semester(self):
        if self.__semmester >= 9:
            return
        self.__semmester = self.__semmester + 1

    def get_name(self):  # Methode ist eine Funktion die sich auf eine classe bezieht! (get_name ist eine methode)
        print(self.firstName + " " + self.lastName + ": " + str(self.age) + " (Semester: " + str(self.__semmester) + ")")

    # oder ich kann auch weitere funktionen(methode) zu den instanzen dazu geben
    # die ich dann zu den instanzen einfügen könnte
    def berechtigung(self):
        if self.age >= 1 and self.age <= 5:
            print("Du bist eher für den Kindergarten!")
        elif self.age <= 0:
            print("Seehr jung!")
        elif self.age >= 18:
            print("Du darfst Studieren!")
        else:
            print("Du musst dein alter angeben!")


son = Student("Adis", "Cajlakovic", 4)  # son oder daughter ist eine Instanz für die nachfolgende eigenschaft
son.eingeschriebenes_semester()
son.__semmester = 10 # self.semmester im konstruktor wird hiermit versucht zu überschreiben
# wenn ich aber einen doppelten unteschtrich setze, ist diese variabel nun schreibgeschützt
# und kann nur innerhalb der classe geändert werden!
son.get_name()  # hiermit rufe ich eine Methode auf oder eine funktion in einer classe
son.berechtigung()

# daughter = Student("Emma", "Cajlakovic", 0)
# daughter.get_name()
# daughter.berechtigung()
#
# mama = Student("Enida", "Cajlakovic", 35)
# mama.get_name()
# mama.berechtigung()
#
# babo = Student("Elvedin", "Cajlakovic", 34)
# babo.get_name()
# babo.berechtigung()
