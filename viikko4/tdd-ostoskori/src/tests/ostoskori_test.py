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