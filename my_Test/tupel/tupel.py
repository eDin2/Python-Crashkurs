tupel = (1, 2, 3)
print(tupel)

# Tupel kann nicht beschrieben werden!
# in eine Liste z.Bsp. können immer wieder werte eingetragen werden


# Tupe packen und entpacken!!
# ###########################
student = ("Max", 22, "Informatik")
name, alter, fach = student
# name = student[0]
# alter = student[1]
# fach = student[2]

print(name)
print(alter)
print(fach)


# wenn du tupel als parameter in eine Funktion übergeben müchtest
def get_student():
    return ("Max", 22, "Informatik")
name, alter, fach = get_student()
print(name)
print(alter)
print(fach)

# eine liste mit tupeln kann mit einer schleife ausgegebn werden!
# und diese könne auch entpackt werden
students = [
    ("Saban Saulic", 65),
    ("Safet Idovic", 85)
]

# oder auch schnellere wariante!
for name, alter in students:
    print(name)
    print(alter)

# ergibt das selbe wie:
# for student in students:
#     name, alter = student
#     print(name)
#     print(alter)


