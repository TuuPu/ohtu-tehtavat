KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None or not self.kapasiteetin_ja_kasvatuskoon_tarkistus(kapasiteetti):
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti
        if kasvatuskoko is None or not self.kapasiteetin_ja_kasvatuskoon_tarkistus(kasvatuskoko):
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kapasiteetin_ja_kasvatuskoon_tarkistus(self, annettu_arvo):
        if not isinstance(annettu_arvo, int) or annettu_arvo < 0:
            return False
        return True

    def kuuluu(self, n):
        luku_loyty = False
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                luku_loyty = True
                return luku_loyty
        return luku_loyty

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.tee_uusi_taulukko()
            return True
        return False

    def tee_uusi_taulukko(self):
        kasvatettu = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(self.ljono, kasvatettu)
        self.ljono = kasvatettu


    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                self.siirra_elementti_poistetun_tilalle(i)
                return True
        return False

    def siirra_elementti_poistetun_tilalle(self, elementti):
        for i in range(elementti, self.alkioiden_lkm - 1):
            apu = self.ljono[i]
            self.ljono[i] = self.ljono[i + 1]
            self.ljono[i + 1] = apu
        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    def print_joukko(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            lukujono = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                lukujono = lukujono + str(self.ljono[i]) + ", "
            lukujono = lukujono + str(self.ljono[self.alkioiden_lkm -1]) + "}"
            return lukujono

    @staticmethod
    def yhdiste(a, b): #Korjaus mahdollinen, jos saa union-funktiolla suoraan yhdisteen?
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])
        return x

    @staticmethod
    def leikkaus(a, b): #Sama, kun yhdisteen kanssa
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])
        return y

    @staticmethod
    def erotus(a, b): #Tsekkaa vielä tämäkin
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        return self.print_joukko()

