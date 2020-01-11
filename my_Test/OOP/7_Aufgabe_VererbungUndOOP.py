class FileReader():
    def __init__(self, fileName):
        self.fileName = fileName

    def lines(self):  # hiermit wird die datei eingelesen
        people = []  # 2 erstelle eine leere liste
        with open(self.fileName, "r") as file:  # 1 datei öffnen mit "r"
            for name in file:  # 3 gehe die geöffnete datei mit einer for schleife durch
                people.append(name.strip())  # 4 appende die Namen in die liste people ein
                # mit strip werden die backslashs entfernt
        return people  # 5 gibt den wert zurück


class CsvReader(FileReader): # diese classe sollte mit der classe FileReader erweitert werden
    def __init__(self, fileName):
        super().__init__(fileName)

    def lines(self):  # hiermit wird die datei eingelesen
        people = []  # 2 erstelle eine leere liste
        with open(self.fileName, "r") as file:  # 1 datei öffnen mit "r"
            for name in file:  # 3 gehe die geöffnete datei mit einer for schleife durch
                people.append(name.strip().split(","))  # 4 appende die Namen in die liste people ein
                # mit strip werden die backslashs entfernt
                # mit split werden diese am komma geternnt und ergeben ein liste in liste
        return people  # 5 gibt den wert zurück




f = FileReader('datei.csv')
print(f.lines())

print("##################################################")

f = CsvReader('datei.csv')
print(f.lines())
