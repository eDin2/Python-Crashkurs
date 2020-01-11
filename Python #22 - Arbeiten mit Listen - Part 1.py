liste = [1, 2, 3, 4, 5]

# Einfaches kopieren der Liste
bearbeitete_liste = [x for x in liste]
print("\nUnbearbeitet: ", bearbeitete_liste, "\n")

# Kopiere die Liste, aber multipliziere jedes Element mit 10
bearbeitete_liste = [x * 10 for x in liste]
print("Mit 10 multipliziert: ", bearbeitete_liste, "\n")

# Kopiere die Liste, aber konvertiere jedes Element zu einem float
bearbeitete_liste = [float(x) for x in liste]
print("Zu float konvertiert:", bearbeitete_liste, "\n")

# Kopiere die Liste, aber nur die Elemente, die durch 2 teilbar sind
bearbeitete_liste = [x for x in liste if x % 2 == 0]
print("Elemente die durch 2 teilbar sind: ", bearbeitete_liste, "\n")

# Füge zu jeder Unterliste eine 10 hinzu
liste_von_listen = [ [1,2], [3,4], [5,6] ]
[x.append(10) for x in liste_von_listen]
print("10 angefügt: ", liste_von_listen, "\n")

# Kopiere die Liste, aber verdoppele jedes Element jeder Unterliste
liste_von_listen = [ [1,2], [3,4], [5,6] ]
bearbeitete_liste = [ [y * 2 for y in x] for x in liste_von_listen]
print("Alle einzelnen Elemente verdoppelt: ", bearbeitete_liste, "\n")

# Betrachte nur Listen mit genau 3 Elementen
# Aus denen betrachte nur durch 2 teilbare Elemente
# Teile diese Elemente durch 2 und konvertiere sie zu Integern
lvl = [ [1,2], [3,4,5], [6,7,8] ]
bl = [ [int(y / 2) for y in x if y % 2 == 0] for x in lvl if len(x) == 3]
print("Bearbeitete Liste: ", bl, "\n")