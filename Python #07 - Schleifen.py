# Zahlen von 17 bis 41 (!) durchlaufen
# Kurze Version: range(...)
for lieblingszahl in range(17, 42):
    if (lieblingszahl % 2 == 0): # Nur gerade Zahlen
        print(lieblingszahl)

# "Solange" die Bedingung wahr ist...tue
eingabe = str(input("Eingabe: "))
while (eingabe != "tschüss"):
    print("Selber " + eingabe)
    eingabe = str(input("Eingabe: "))
