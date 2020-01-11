# ### Aufgabe 2: Modelliere ein Kugel
# Die Kugel-Klasse soll als Eigenschaft den Radius übergeben bekommen.
# Zudem soll sie - ähnlich wie der Würfel - zwei Methoden haben: `surface()`
# um den Oberflächeninhalt zu berechnen, `volume()` um das Volumen zu berechnen.
#
# Damit du diese Berechnungen durchführen kannst, benötigst du die Kreiszahl Pi.
# Diese steht dir nach einem `import math` unter `math.pi` zur Verfügung
# (was der `import` - Befehl genau macht, schauen wir uns noch später im Kurs an).
#
# Die Formeln für den Oberflächeninhalt / das Volumen einer Kugel darfst du im Internet nachgucken.
import math

print(math.pi)


# pi = math.pi


class Ball():
    def __init__(self, radius):  # konstruktor!
        self.radius = radius

    # Umfang Kugel
    # U = 2⋅π⋅r = π⋅d

    # Volumen Kugel
    # V = 4/3⋅π⋅r3
    def volume(self):  # Methode volume
        print(4 / 3 * math.pi * self.radius ** 3)
        return

    # Oberfläche Kugel
    # O = 4⋅π⋅r2
    def surface(self):  # Methode surface
        print(4 * math.pi * self.radius ** 2)
        return


# Ergänze hier deinen Code


b = Ball(4)
b.surface()
b.volume()

# Erwartete Ausgabe (es reicht, wenn die Zahlenwerte auf ein paar Nachkommastellen genau sind):
#
# ```
# 201.06192982974676
# 268.082573106329
# ```
