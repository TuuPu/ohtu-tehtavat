import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
#3. Yhden tuotteen lisäämisen jälkeen ostoskorin hinta on sama kuin tuotteen hinta.
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
#4. Kahden eri tuotteen lisäämisen jälkeen ostoskorissa on 2 tavaraa
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        kaali = Tuote("Kaali", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kaali)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
#5. Kahden eri tuotteen lisäämisen jälkeen ostoskorin hinta on sama kuin tuotteiden hintojen summa
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        kaali = Tuote("Kaali", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(kaali)
        self.assertEqual(self.kori.hinta(), 8)
#6. Kahden saman tuotteen lisäämisen jälkeen ostoskorissa on 2 tavaraa
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
#7. Kahden saman tuotteen lisäämisen jälkeen ostoskorin hinta on sama kuin 2 kertaa tuotteen hinta
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)
    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
#9. Yhden tuotteen lisäämisen jälkeen ostoskori sisältää ostoksen, jolla sama nimi kuin tuotteella ja lukumäärä 1

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_ostoksen_jolla_on_sama_nimi_kuin_tuotteella_ja_lkm1(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)
#10. Kahden eri tuotteen lisäämisen jälkeen ostoskori sisältää kaksi ostosta
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
#11. Kahden saman tuotteen lisäämisen jälkeen ostoskori sisältää yhden ostoksen
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset =  self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
#12. Kahden saman tuotteen lisäämisen jälkeen ostoskori sisältää ostoksen
# jolla sama nimi kuin tuotteella ja lukumäärä 2
    def test_kahden_saman_tuotteen_lisaaminen_sisaltaa_ostoksen_jolla_sama_nimi_kuin_tuotteella_ja_lkm2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)