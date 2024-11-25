import unittest
from unittest.mock import Mock
from tuote import Tuote

class TestTuote(unittest.TestCase):

    def setUp(self):
        self.tuote1 = Tuote(1, "Maito", 1.50)
        self.tuote2 = Tuote(2, "Leipä", 2.00)
        self.tuote3 = Tuote(1, "Maito", 1.50)

    def test_tuote_eq_same_id(self):
        self.assertTrue(self.tuote1 == self.tuote3)

    def test_tuote_eq_different_id(self):
        self.assertFalse(self.tuote1 == self.tuote2)

    def test_tuote_eq_mock(self):
        mock_tuote = Mock(spec=Tuote)
        mock_tuote.id = 1
        self.assertTrue(self.tuote1 == mock_tuote)
