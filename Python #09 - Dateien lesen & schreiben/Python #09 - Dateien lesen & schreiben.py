# Aus Datei lesen (r = read)
my_file = open("savegame.dat", "r")
lines = my_file.read().splitlines()

for line in lines:
    print(line)
# Datei schließen
my_file.close()

# In Datei schreiben (w = write)
my_file = open("savegame.dat", "w")
savegame_daten = ["Boaty McBoatface", "100HP",
                  "Der gewaltige Stamm des Mammutbaumes"]

for line in savegame_daten:
    my_file.write(line + "\n")  # \n = neue Zeile

my_file.close()

# An Datei anfügen (a = append)
my_file = open("savegame.dat", "a")
my_file.write("1 Mio. Mana")

my_file.close()
