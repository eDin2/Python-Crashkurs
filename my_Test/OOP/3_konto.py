# ### Aufgabe 3: Modelliere ein Konto
#
# #### a.)
# Erstelle die Konto-Klasse _Account_ mit der Eigenschaft Kontostand _credits_! Diese Eigenschaft wird mit einem Startkapital initialisiert.
# Die Methode `display()` soll den aktuellen Kontostand ausgeben.
class Account():
    def __init__(self, kunde):
        self.kunde = kunde

    def credits(self):
        pass

    def display(self):
        print(self.kunde)


# Ergänze hier deinen Code

Kunde111 = Account(500)
Kunde111.display()


# Erwartete Ausgabe:
#
# ```
# 500
# ```

# **b.)**
# Ergänze die Klasse _Account_ um zwei Methoden (`pay_in()` zum Einzahlen, `withdraw()` zum Abheben),
# so dass du Geldbeträge einzahlen und abbuchen kannst, und der Kontostand entsprechend angepasst wird.
#
# Du sollst nur Geld abheben können, so lange auch Geld auf dem Konto ist. Ein Dispo-Kredit wird nicht gewährt.
# In dem Fall soll eine Fehlermeldung ausgegeben werden, in der steht, wieviel Geld maximal abgebucht werden kann.
class Account():


# Ergänze hier deinen Code. Du darfst den Code aus a)
# natürlich hierhin übernehmen.


Kunde111 = Account(500)
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25)
Kunde111.display()
Kunde111.withdraw(600)


# Erwartete Ausgabe:
#
# ```
# 500
# 540
# 515
# Du kannst nur noch 515€ abheben!
# ```

# **c.)**
# Bislang ist das Konto noch ungeschützt - wir brauchen eine PIN! Ergänze in der Klasse die Eigenschaft _pin_!
# So wie mit dem Startkapital soll das Konto auch mit einer PIN initialisiert werden.
#
# Von nun an muss man beim Geldabheben nicht nur den Betrag, sondern auch die PIN angeben:
# Nur wenn die PIN mit der des Kontos übereinstimmt,
# kann auch Geld abgebucht werden, ansonsten kommt es zu einer Fehlermeldung!
class Account():


# Ergänze hier deinen Code. Du darfst den Code aus b)
# natürlich hierhin übernehmen.


Kunde111 = Account(500, "1234")
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25, "1234")
Kunde111.display()
Kunde111.withdraw(600, "12345")

# Erwartete Ausgabe:
#
# ```
# 500
# 540
# 515
# Falsche PIN! Konto gesperrt! Du bist verhaftet! Hände hoch!
# ```
