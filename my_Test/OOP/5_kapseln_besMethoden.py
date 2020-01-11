class PhoneBook():
    def __init__(self):  # solange hier keine änderungen sind
        # hat die funktion noch die selbe funktion wie zufor
        self.__entries = {}  # mit den unteschtrichen kann ich von aussen nicht darauf zugreifen

    def add(self, name, phone_number):  # solange hier keine änderungen sind
        # hat die funktion noch die selbe funktion wie zufor
        # alle anweisungen können nach beliben geändert werden
        self.__entries[name] = phone_number

    def get_number(self, name):  # solange hier keine änderungen sind
        # hat die funktion noch die selbe funktion wie zufor
        # alle anweisungen können nach beliben geändert werden
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None

    def __str__(self):
        return "PhoneBook" + str(self.__entries)

    def __len__(self):
        return len(self.__entries)


# wenn jetzt z.Bsp. mein Kollege einen weiteren eintragtätigt, dann wird es zu keinem Fehler aufkommen!
book = PhoneBook()
book.add("Mustermann", "+436546432")
book.add("Saban", "+385465161")

print(book.get_number("Mustermann"))  # => ausgabe kommt die Nummer von Mustermann
print(book.get_number("Edo"))  # => kommt die ausgabe None

print(book)
# wenn ich versuche die zu debuggen kommt wie folgt <__main__.PhoneBook object at 0x0000028CD6D88430>
# wenn ich aber eine def mit __str__ erstelle die erwas returnt kommt wie folgen die einträge aus dem dict.. self.entr..

print(len(book))
# mit def __len__ wird die länge der einträge im self.__entries ausgegeben
