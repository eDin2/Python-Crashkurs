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


def main():
    mein_tier = Tier("Frank", 7)
    mein_tier.print_info()


if __name__ == "__main__":
	main()
