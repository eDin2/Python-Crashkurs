# file = open("lesen.txt", "r")
# for line in file:
#     print(line.strip())

# with open("lesen.txt", "r") as file:
#     for line in file:
#         print(line.strip())
# #####################################################################


# #####################################################################
# with open("lesen_my.txt", "a") as file:
#     students = ["Adis", "Enida", "Edo", "Emma"]
#     # Wir loopen mit einer for-Schleife durch die Liste students
#     for student in students:
#         # Mit der write-Methode schreiben wir den aktuellen String student und einen Zeilenumbruch in das file-Objekt
#         file.write(student + "\n")
# #####################################################################



# in txt file schreiben
# #####################################################################
# def file_write():
#     with open("lesen_my.txt", "a") as file:
#         students = ["Saban", "Enida", "Edo", "Emma"]
#         # Wir loopen mit einer for-Schleife durch die Liste students
#         for student in students:
#             # Mit der write-Methode schreiben wir den aktuellen String student und einen Zeilenumbruch in das file-Objekt
#             file.write(student + "\n")
# file_write()
# ##############################################


# #####################################################################
# txt file auslesen
# #####################################################################
# def file_open():
#     with open("lesen_my.txt", "r") as file:
#         # Wir loopen mit einer for-Schleife durch die Liste students
#         for line in file:
#             print(line.strip())
# file_open()
# ##############################################



# funktionen als funktion übergeben!
# ##############################################
# def parameter(name, count):
#     for i in range(0, count):
#         print(name)
# # parameter("Hallo", 3) # mit dem auskommentieren wird die ausführung unterbrochen!
# # funktion mit mehreren Parametern => Zähler als parameter der in der for schleife bearbeitet wird
#
# # oder funktion in funktion ausführen
# def calback_funktion():
#     parameter("Hallo", 2)
#     parameter("Welt", 2)
# calback_funktion()
# ################################################################
# def maximum(a, b):
#     if a < b:
#         return b
#     else:
#         return a
# ausgabe = maximum(3, 4) # parameter werden die die varaibel "ausgabe"
# print(ausgabe)
# ################################################################

# ################################################################
with open("tabelle.csv", "r") as file:
    for i in file:
        data = i.strip().split(";")
        # print(data)
        print(data[0] + ":" + data[1])
        if int(data[1]) >= 30:
            print("alle die über 30 sind, sind voll alt!")
        elif int(data[1]) <= 4:
            print("zu jung!")