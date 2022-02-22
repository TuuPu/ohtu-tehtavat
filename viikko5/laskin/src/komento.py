class Summa:
    def __init__(self, sovellus, reader):
        self.sovellus = sovellus
        self.reader = reader

    def suorita(self):
        arvo = int(self.reader())
        self.sovellus.plus(arvo)


class Erotus:
    def __init__(self, sovellus, reader):
        self.sovellus = sovellus
        self.reader = reader

    def suorita(self):
        arvo = int(self.reader())
        self.sovellus.miinus(arvo)

class Nollaa:
    def __init__(self, sovellus, reader):
        self.sovellus = sovellus
        self.reader = reader

    def suorita(self):
        self.sovellus.nollaa()

class Lopeta:
    def __init__(self, io):
        self.io = io

    def suorita(self):
        self.io.kirjoita("Kiitos ja näkemiin!")
        sys.exit(0)