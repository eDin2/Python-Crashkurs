# Funktion mit 2 optionalen Parametern
def adress_daten(name, stadt, strasse, nummer, land="Deutschland", anmerkung=""):
    print("\n-----")
    print(name)
    print("Wohnhaft:")
    print(stadt)
    print(strasse + " " + nummer)
    print(land)
    print(anmerkung)
    print("-----\n")

adress_daten("Agathe Bauer", "Berlin", "Willy-Brandt-Straße", "1", anmerkung="Spielt gerne mit Sekundenkleber")
adress_daten("Awontse Bauer", "New York", "5th Ave", "725", "USA", "Hat kleine Hände")

# Funktion durchläuft eine Liste und wendet eine übergebene Funktion auf alle Elemente der Liste an
def liste_durchlaufen(liste, funktion):
    print("\n-----")
    for element in liste:
        funktion(element)
    print("-----\n")

def verdoppeln_ausgeben(zahl):
    print(zahl * 2)

def quadrieren_ausgeben(zahl):
    print(zahl ** 2)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

liste_durchlaufen(liste, verdoppeln_ausgeben)
liste_durchlaufen(liste, quadrieren_ausgeben)
    
