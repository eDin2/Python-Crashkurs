liste = [3, 1, 2, 5, 4]

print( "\nGrößtes Element der Liste: ", max(liste), "\n" )

print( "Kleinstes Element der Liste: ", min(liste), "\n" )

print( "Sortierte Liste: ", sorted(liste), "\n" )

# Anonyme Funktion anlegen
funktion = lambda x : (x + 5) * 2
print( "funktion(2): ", funktion(2), "\n" )

ergebnis = list( map(funktion, liste) )
print( "map Ergebnis: ", ergebnis, "\n" )

liste_2 = [4, 6, 5, 2, 3]
ergebnis = list( map(lambda x,y : x + y, liste, liste_2) )
print( "map mit 2 Listen Ergebnis: ", ergebnis, "\n")

print( "Summe aller Elemente: ", sum(liste), "\n" )

namens_liste = ["Berta", "Albert", "Charlie", "Else", "Dieter"]
print("Sortierte Namens-Liste: ", sorted(namens_liste), "\n" )

snl = sorted(namens_liste, key= lambda x: x[1] )
print("Sortiert n. zweiten Buchstaben: ", snl, "\n" )