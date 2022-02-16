from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = []

    def tavaroita_korissa(self):
        if not self.ostoslista:
            return 0
        tuotemaara = 0
        for ostos in self.ostoslista:
            tuotemaara += ostos.lukumaara()
        return tuotemaara

    def hinta(self):
        arvo = 0
        for i in self.ostoslista:
            arvo += i.hinta()
        return arvo

    def lisaa_tuote(self, lisattava: Tuote):
        loyty = False
        for i in self.ostoslista:
            if i.tuotteen_nimi() == lisattava.nimi():
                i.muuta_lukumaaraa(1)
                loyty = True
        if loyty is False:
            self.ostoslista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        loyty = False
        for i in self.ostoslista:
            if i.tuotteen_nimi() == poistettava.nimi():
                i.muuta_lukumaaraa(-1)
                loyty = True
        if loyty is False:
            return

    def tyhjenna(self):
        self.ostoslista.clear()

    def ostokset(self):
        return self.ostoslista
