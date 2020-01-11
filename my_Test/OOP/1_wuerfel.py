# ### Aufgabe 1: Modelliere einen Würfel

# Erstelle eine Klasse _Cube_, mit der du einen Würfel modellierst!
# Die Würfel-Klasse soll als Eigenschaft die Länge einer Würfel-Seite besitzen.
# Darüber hinaus soll die Klasse auch zwei Methoden haben:
# die Methode `volume()` berechnet das Volumen und gibt es aus,
# die Methode `surface()` berechnet die Oberfläche und gibt sie aus.
class Cube():
    def __init__(self, laenge):  # konstruktor!
        self.laenge = laenge

    def volumen(self):  # Methode volume
        # self.laenge = self.laenge * self.laenge * self.laenge
        print(self.laenge ** 3)
        return

    def surface(self):  # Methode surface
        # self.laenge = 6 * self.laenge * self.laenge
        print(6 * self.laenge ** 2)
        return


# danach erzeugen wir eine Instanz deiner Cube-Klasse
a = Cube(3)  # die 3 wird als Parameter in den konstruktor übergeben

# und testen die Methoden
a.volumen()
a.surface()

# Erwartete Ausgabe:
#
# ```
# 27
# 54
# ```
