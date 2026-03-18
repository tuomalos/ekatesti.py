class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdyta(self, muutos):
        self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + muutos
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
    def kulje(self, tuntimaara):
        self.kuljettu_matka = self.kuljettu_matka + self.kuljettu_matka * tuntimaara



uusiauto = Auto("ABC-123",142)


print(f"Auton rekisteri on {uusiauto.rekisteri}")
print(f"Auton huippunopeus on {uusiauto.huippunopeus}")
print(f"Auton tämän hetkinen nopeus on {uusiauto.tamanhetkinen_nopeus}")
print(f"Auton kuljettu matka on {uusiauto.kuljettu_matka}")
uusiauto.kiihdyta(30)
uusiauto.kiihdyta(70)
uusiauto.kiihdyta(50)
print(f"Kiihdytysten jälkeinen nopeus on {uusiauto.tamanhetkinen_nopeus}")
uusiauto.kiihdyta(-200)
