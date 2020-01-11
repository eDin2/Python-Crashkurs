def schlaue_funktion():
	print("Hier arbeitet die Funktion des Moduls mit main")

# Der Hauptteil ist hier in eine Funktion ausgelagert
def main():
	print("Hier arbeitet der Hauptteil des Moduls mit main")

# Prüft ob diese Datei direkt ausgeführt wird (oder nur importiert wird)
if (__name__ == "__main__"):
	main()