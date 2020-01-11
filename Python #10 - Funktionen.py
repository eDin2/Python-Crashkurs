def add():
    zahl_1 = float(input("Zahl 1: "))
    zahl_2 = float(input("Zahl 2: "))
    print(zahl_1 + zahl_2)


def sub():
    zahl_1 = float(input("Zahl 1: "))
    zahl_2 = float(input("Zahl 2: "))
    return zahl_1 - zahl_2


def mul(zahl_1, zahl_2):
    print(zahl_1 * zahl_2)


def div(zahl_1, zahl_2):
    return zahl_1 / zahl_2


print("Ergebnis der Addition: ")
add()

print("Ergebnis der Subtraktion: " + str(sub()))

print("Ergebnis der Multiplikation: ")
mul(3.1415, 2)

print("Ergebnis der Division: " + str(div(42, 7)))
