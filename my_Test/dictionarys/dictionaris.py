l = {"Bosna & Hercegeovina": "Sarajevo", "Austria": "Vienna", "Slovenia": "Maribor"}

# print(l["Austria"])

del l["Slovenia"]
l["Saban"] = "Saulic"

eingabe = input("Zu welchem Land brauchen Sie die Hausptstadt? : ")
if eingabe in l:
    print(l["Bosna & Hercegeovina"])
elif eingabe == "Austria":
    print(l["Austria"])
elif eingabe == "Slovenia":
    print("Slovenia gibt es nicht!")
else:
    print("Zu dumm um ein Land einzugeben?")

# DICTIONARYS UND SCHLEIFEN!!
ld = {
    "Ägypten": "Kairo",
    "Angola": "Luanda",
    "Japan": "Tokio",
    "Bosnien": "Sarajevo",
    "Deutschland": "Berlin",
    "Austria": "Vienna"
}

for land in ld:
    hauptStadt = (ld[land])
    print(land)
    print(hauptStadt)

print(ld.items()) # Ausgabe des dictionariys als eine liste mit tupeln
# dict_items([('Ägypten', 'Kairo'), ('Angola', 'Luanda'), ('Japan', 'Tokio'), ('Bosnien', 'Sarajevo'), ('Deutschland', 'Berlin'), ('Austria', 'Vienna')])

# dies können dieses dictionarys wie eine liste mit tupeln bhandlen
# (siehe dazu übungsblatt tupel.py)
for land, hauptStadt in ld.items():
    print(land + ": " + hauptStadt)
