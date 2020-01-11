# Liste erstellen
spieler_namen = ["L33T H4X0R", "UnnamedNewbie", "hans wurst"]
spieler_punkte = [1337, 0, 7]

# Auf Liste zugreifen
for i in range(0, len(spieler_namen)): # Länge der Liste mit len()
	print(spieler_namen[i] + " hat " + str(spieler_punkte[i]) + " Punkte.")

# Einträge hinzufügen
spieler_namen.append("xX TheKing99 Xx")
spieler_punkte.append("0")
print(spieler_namen)
print(spieler_punkte)

# Teilisten
Team_A = spieler_namen[0:2]
Team_B = spieler_namen[2:3]

# Eine Liste kann verschiedene Datentypen enthalten
neue_spieler_punkte = [42, "keine", 3.1415, "keine"]
# Ausgeben von Anfang bis Element mit Nummer 1
print("Team A hat " + str(neue_spieler_punkte[:2]) + " Punkte.")
# Ausgeben von Element mit Nummer 2 bis Ende
print("Team B hat " + str(neue_spieler_punkte[2:]) + " Punkte.")

# Ist ... in der Liste?
if("keine" in neue_spieler_punkte):
	print("nOOBs anwesend.")

# Einträge entfernen
print(spieler_namen)
neue_spieler_punkte.remove("keine")
spieler_namen.remove("UnnamedNewbie")
spieler_namen.remove("xX TheKing99 Xx")
print(spieler_namen)
