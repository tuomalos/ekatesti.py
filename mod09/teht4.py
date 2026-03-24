import random
from random import randint


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



autot = []
for i in range(1,11):
    rekisteri = (f"ABC-{i}")
    arvottu_huippunopeus = randint(100,200)
    #uusiauto = Auto(rekisteri, arvottu_huippunopeus)
    autot.append(Auto(rekisteri, arvottu_huippunopeus ))

for auto in autot:
    print(auto.rekisteri, auto.huippunopeus)

