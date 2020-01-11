class Pijevaci():
    def __init__(self):
        self.__estrada = {}

    def add(self, ime, prezime, godine):
        self.__estrada[ime] = godine, prezime

    def get_name(self, ime, prezime, godine):
        if ime or prezime in self.__estrada:
            return self.__estrada[godine]
        else:
            return None


novaGodina = Pijevaci()
novaGodina.add("Saban", "Saulic", 65)
novaGodina.get_name("Saban", "Saulic", 65)