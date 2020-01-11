if(3 < 5): # <- Doppelpunkt
	print("3 ist kleiner als 5") # Wichtig: Einrückung!

if(5 < 3):
	print("5 ist kleiner als 3")
	print("Eine zweite Zeile")

# Alle Operatoren == != <= >= < >

# Eingabe vom Benutzer einlesen
# "Zur Sicherheit" in int umwandeln
zahl = int(input("Eingabe: "))

# Testen auf Gleichheit und Ungleichheit
if(zahl == 42):
	print("Eingabe ist 42.")
if(zahl != 42):
	print("Eingabe ist nicht 42.")

# falls ... ansonsten
if(zahl == 42):
	print("Eingabe ist 42.")
else:
	print("Eingabe ist nicht 42.")

# falls ... andernfalls ... ansonsten
if(zahl == 42):
	print("Eingabe ist 42.")
elif(zahl > 42):
	print("Eingabe ist groesser als 42.")
else:
	print("Eingabe ist nicht 42 und nicht groesser als 42.")

# Falls mindestens eine der beiden wahr
if(zahl == 42 or zahl == 7):
	print("Eingabe ist 42 oder 7.")

# Falls beide wahr
if((zahl != 42) and (zahl != 7)):
	print("Eingabe ist nicht 42 und nicht 7.")

# Wahrheitswerte als Variablen
wahrheitswert = True # False wäre auch möglich
if(wahrheitswert):
	print("Wahr")
