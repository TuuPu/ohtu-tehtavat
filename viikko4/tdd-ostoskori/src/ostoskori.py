from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if not self.ostoslista:
            return 0
        tuotemaara = 0
        for ostos in self.ostoslista:
            tuotemaara += ostos.lukumaara()

        return tuotemaara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        arvo = 0
        for i in self.ostoslista:
            arvo += i.hinta()
        return arvo
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        loyty = False
        for i in self.ostoslista:
            if i.tuotteen_nimi() == lisattava.nimi():
                i.muuta_lukumaaraa(1)
                loyty = True
        if loyty is False:
            self.ostoslista.append(Ostos(lisattava))


        # lisää tuotteen


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoslista
