# Klasse namens 'Tier' erstellen
class Tier:

	# Konstruktor für 'Tier'
	def __init__(self, name_parameter, alter_parameter):
		self.name = name_parameter
		self.alter = alter_parameter

	# Eigene Funktion für 'Tier'
	def print_info(self):
		print(self.name)
		print(self.alter)


# Klasse namens 'Katze', die von 'Tier' erbt
class Katze(Tier):

	# Konstruktor für 'Katze' mit 3 Parametern
	def __init__(self, name, alter, rasse):
		super().__init__(name, alter)
		self.rasse = rasse

	# Eigene Funktion für 'Katze', welche die Funktion von Tier überschreibt
	def print_info(self):
		print(self.name)
		print(self.alter)
		print(self.rasse)


def main():
	meine_katze = Katze("Garfield", 38, "Red Mackerel Tabby Exotic Shorthair")
	meine_katze.print_info()

if __name__ == "__main__":
	main()