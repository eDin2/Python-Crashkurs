class PhoneBook():
    def __init__(self): # solange hier keine änderungen sind
        # hat die funktion noch die selbe funktion wie zufor
        self.__entries = {} # mit den unteschtrichen kann ich von aussen nicht darauf zugreifen

    def add(self, name, phone_number): # solange hier keine änderungen sind
        # hat die funktion noch die selbe funktion wie zufor
        # alle anweisungen können nach beliben geändert werden
        self.__entries[name] = phone_number

    def get_number(self, name): # solange hier keine änderungen sind
        # hat die funktion noch die selbe funktion wie zufor
        # alle anweisungen können nach beliben geändert werden
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None

# wenn jetzt z.Bsp. mein Kollege einen weiteren eintragtätigt, dann wird es zu keinem Fehler aufkommen!
book = PhoneBook()
book.add("Mustermann", "+436546432")
book.add("Saban", "+385465161")

print(book.get_number("Mustermann"))  # => ausgabe kommt die Nummer von Mustermann
print(book.get_number("Edo")) # => kommt die ausgabe None
