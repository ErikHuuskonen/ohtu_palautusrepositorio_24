import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.kirjanpito_mock = Mock()
        self.varasto = Varasto(self.kirjanpito_mock)

    def test_hae_tuote_loytyy(self):
        tuote = self.varasto.hae_tuote(1)
        self.assertEqual(tuote.nimi, "Koff Portteri")

    def test_hae_tuote_ei_loydy(self):
        tuote = self.varasto.hae_tuote(999)
        self.assertIsNone(tuote)

    def test_saldo_oikein(self):
        saldo = self.varasto.saldo(1)
        self.assertEqual(saldo, 100)

    def test_ota_varastosta_vahentaa_saldoa(self):
        tuote = self.varasto.hae_tuote(1)
        self.varasto.ota_varastosta(tuote)
        self.assertEqual(self.varasto.saldo(1), 99)
        self.kirjanpito_mock.lisaa_tapahtuma.assert_called_with(f"otettiin varastosta {tuote}")

    def test_palauta_varastoon_kasvattaa_saldoa(self):
        tuote = self.varasto.hae_tuote(1)
        self.varasto.ota_varastosta(tuote)
        self.varasto.palauta_varastoon(tuote)
        self.assertEqual(self.varasto.saldo(1), 100)
        self.kirjanpito_mock.lisaa_tapahtuma.assert_called_with(f"palautettiin varastoon {tuote}")