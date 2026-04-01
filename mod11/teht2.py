class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankki):
        super().__init__(rekisteri, huippunopeus)
        self.bensatankki = bensatankki



sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
moottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.tamanhetkinen_nopeus = 70
moottoriauto.tamanhetkinen_nopeus = 90
print(f"sähköauton aloitus nopeus on {sahkoauto.tamanhetkinen_nopeus}")
print(f"moottoriauton aloitus nopeus on {moottoriauto.tamanhetkinen_nopeus}")

sahkoauto.kuljettu_matka = sahkoauto.tamanhetkinen_nopeus * 3
moottoriauto.kuljettu_matka = moottoriauto.tamanhetkinen_nopeus * 3

print(f"3 tunnin matkan jälkeen moottoriauto on kulkenut {moottoriauto.kuljettu_matka}")
print(f"3 tunnin matkan jälkeen sähköauto on kulkenut {sahkoauto.kuljettu_matka}")