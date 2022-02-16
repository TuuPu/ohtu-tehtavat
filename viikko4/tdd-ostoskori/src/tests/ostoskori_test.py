import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
#1.
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
#2.
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
#3.
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
#4.
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        kaali = Tuote("Kaali", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kaali)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
#5.
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        kaali = Tuote("Kaali", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kaali)
        self.assertEqual(self.kori.hinta(), 8)
#6.
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
#7.
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)
#8.
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
#9.

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_on_sama_nimi_kuin_tuotteella_ja_lkm1(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
#10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        kaali = Tuote("Kaali", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kaali)
        ostos1 = self.kori.ostokset()[0]
        ostos2 = self.kori.ostokset()[1]
        self.assertEqual(ostos1.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos2.tuotteen_nimi(), kaali.nimi())
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
#11.
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset =  self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
#12.
    def test_kahden_saman_tuotteen_lisaaminen_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lkm2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)
#13.
    def test_korissa_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jaa_koriin_ostos_jossa_on_tuotetta_1kpl(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.kori.poista_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
#14.
    def test_jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_kori_on_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.kori.poista_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
#15.
    def test_metodi_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(ostokset), 0)