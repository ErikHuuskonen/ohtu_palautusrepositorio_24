KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm >= len(self.ljono):
                self._kasvata_taulukkoa()
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def _kasvata_taulukkoa(self):
        uusi_taulukko = self._luo_lista(len(self.ljono) + self.kasvatuskoko)
        self.kopioi_lista(self.ljono, uusi_taulukko)
        self.ljono = uusi_taulukko

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            kohta = self.ljono.index(n)
            self.ljono[kohta:self.alkioiden_lkm - 1] = self.ljono[kohta + 1:self.alkioiden_lkm]
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, vanha, uusi):
        for i in range(len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            tulos.lisaa(numero)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            tulos.lisaa(numero)
        for numero in b.to_int_list():
            tulos.poista(numero)
        return tulos

    def __str__(self):
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
