class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

uusiauto = Auto("ABC-123",142)


print(f"Auton rekisteri on {uusiauto.rekisteri}")
print(f"Auton huippunopeus on {uusiauto.huippunopeus}")
print(f"Auton tämän hetkinen nopeus on {uusiauto.tamanhetkinen_nopeus}")
print(f"Auton kuljettu matka on {uusiauto.kuljettu_matka}")