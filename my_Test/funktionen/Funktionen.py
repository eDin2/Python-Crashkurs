# Schreibe eine Funktion, die den Gesamtpreis der Produkte im Warenkorb berechnet!
# #############################################################
cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]


def preise_summieren():
    summe = cart_prices[0]  # summe ist erstes Listenelement
    for i in cart_prices[
             1:]:  # Schleife ab dem 2. Element das erste elment wird nicht einbezogen weil er sowiso als erstes
        # elment in die liste :ubertragen wird
        summe += i  # Aufsummieren
        cart_prices.append(summe)  # an die neue Liste "summe" hängen
    print(summe)


preise_summieren()


# Schreibe eine Funktion, die für einen Artikel eine Preis-Tabelle erstellt!
# #############################################################
def prices_list(name, price):
    l = []
    for i in range(1, 11):  # 10 Artikel sollten generiert werden
        l.append(str(i) + "x" + name + ": " + str(price * i))
    return l


print(prices_list("Wunderkeks", 0.79))

# Schreibe eine Funktion, die die liste mit Artikeln befüllen!
# #############################################################
lager = ["Orah", "leer", "Jagoda", "Keks", "Vodka", "leer"]


def add_lager(artikel):
    for i in range(0, len(lager)): # loope die liste von 0 bis länge der liste
        if lager[i] == "leer": # sollte in der liste ein "leer" auftauchen
            # print(i)
            lager[i] = artikel # dann ersetze ihn durch den neuen Artikel
            break # beim ersten "leer" break und warten auf den nächsten eintrag


add_lager("Rakija")
add_lager("Smokva")

print(lager)
# Ausgabe => ['Orah', 'Rakija', 'Jagoda', 'Keks', 'Vodka', 'Smokva']
