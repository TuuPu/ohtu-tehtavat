import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_pelaajan_nimi_loytyy_oikein(self):
        self.assertEqual(self.statistics.search('Semenko').name, 'Semenko')

    def test_pelaajan_nimi_ei_loydy(self):
        self.assertEqual(self.statistics.search('Tapio'), None)

    def test_joukkueen_pelaajat_loytyy(self):
        self.assertEqual(len(self.statistics.team('EDM')), 3)

    def test_pistemies_loytyy(self):
        top=self.statistics.top_scorers(3)[0]
        self.assertEqual(str(top), str(Player("Gretzky", "EDM", 35, 89)))