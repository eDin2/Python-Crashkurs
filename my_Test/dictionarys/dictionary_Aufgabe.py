import csv
with open("names.csv", "r") as liste: # 1 datei öffnen mit "r"
    people = {} # 2 erstelle eine leeres dictionary
    for name in liste: # 3 gehe die geöffnete datei mit einer for schleife durch
        splitted = name.strip().split(",") # mit strip werden die leerzeichen umgangen und mit split ab "," gettrent
        if splitted[0] == "Id": # sollte sich bei dem ersten eintrag um eine 'Id' handlen dann überspringen
            continue # hiermit wird der eintrag "Id" übersprungen
        # print(splitted)
        # break
# in der ersten reihe der datei befindet sich der Tabellenkopf:
# ['Id', 'Name', 'Year', 'Gender', 'State', 'Count']  => dieser teil wird übersprungen

        name = splitted[1] # Name als variabel auf der zweiten stelle befindet sich der Name
        count = int(splitted[5]) # Zähler als variabel auf der sechsten stelle befindet sich die Anzahl=summe

        if name in people: # gibt es den namen im dictionary?
            people[name] = people[name] + count # sollte der name erneut kommen sollte dann zähle um "count" hoch
        else:
            people[name] = count # falls es den Namen nicht gibt dan erstelle ihn um den wert aus "count"
            # der count wert wird immerwieder addiert aber als string, der in ein int umgewandelt werden sollte
# print(people) # alle namen die aus der datei gefiltert wurden

max_anzahl = 0
name = ""
for key, value in people.items():
    if max_anzahl < value:
        max_anzahl = value
        name = key
print(name) # Neme James wurde am heufigsen vorkommenden
print(max_anzahl) # Anzahl der vergebenen Namen
print([name, max_anzahl]) # ausgabe als liste!!!
