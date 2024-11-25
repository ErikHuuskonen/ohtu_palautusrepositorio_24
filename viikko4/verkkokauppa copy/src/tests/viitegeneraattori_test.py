import unittest
from unittest.mock import MagicMock
from viitegeneraattori import Viitegeneraattori

class TestViitegeneraattori(unittest.TestCase):
    def setUp(self):
        self.viitegeneraattori = Viitegeneraattori()

    def test_uusi_palauttaa_oikean_arvon(self):
        self.assertEqual(self.viitegeneraattori.uusi(), 2)
        self.assertEqual(self.viitegeneraattori.uusi(), 3)

    def test_uusi_kasvattaa_seuraavaa(self):
        self.viitegeneraattori.uusi()
        self.assertEqual(self.viitegeneraattori._seuraava, 2)

    def test_uusi_mock(self):
        self.viitegeneraattori.uusi = MagicMock(return_value=10)
        self.assertEqual(self.viitegeneraattori.uusi(), 10)
        self.viitegeneraattori.uusi.assert_called_once()
