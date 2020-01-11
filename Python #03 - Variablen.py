# 3 Variablen anlegen
ganzzahl = 42
kommazahl = 3.14
text = "Das ist ein String"

# Variablen ausgeben
print(ganzzahl)
print(kommazahl)
print(text)

# Typen der Werte in den Variablen
print(type(ganzzahl))
print(type(kommazahl))
print(type(text))

# 3 Variablen anlegen (Kurze Version)
a, b, c = 7, 42, "Hallo!!"

# 2 Zahlen addieren mit +
neueZahl = ganzzahl + kommazahl
print(neueZahl)
print(type(neueZahl))

# 2 Strings verknüpfen (konkatenieren) mit +
text2 = "Das ist der Anfang " + "Das ist das Ende"
print(text2)
print(len(text2))

# Umwandeln von Typen
text3 = "5"
print(text2 + text3)
print(int(text3) + ganzzahl)

# Umwandeln des Typs zum Abrunden
print(int(kommazahl))