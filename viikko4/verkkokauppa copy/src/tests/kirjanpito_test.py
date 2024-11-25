import unittest
from unittest.mock import MagicMock
from kirjanpito import Kirjanpito

class TestKirjanpito(unittest.TestCase):
    def setUp(self):
        self.kirjanpito = Kirjanpito()

    def test_lisaa_tapahtuma(self):
        tapahtuma = "Testitapahtuma"
        self.kirjanpito.lisaa_tapahtuma(tapahtuma)
        self.assertIn(tapahtuma, self.kirjanpito.tapahtumat)

    def test_lisaa_tapahtuma_mock(self):
        tapahtuma = "MockTapahtuma"
        self.kirjanpito.lisaa_tapahtuma = MagicMock()
        self.kirjanpito.lisaa_tapahtuma(tapahtuma)
        self.kirjanpito.lisaa_tapahtuma.assert_called_with(tapahtuma)
