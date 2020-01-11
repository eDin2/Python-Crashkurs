try:
	eingabe = int(input())
	datei = open("keineDatei.txt")
except ValueError:
	print("Keine Zahl!")
except FileNotFoundError:
	pass # Mache nichts
