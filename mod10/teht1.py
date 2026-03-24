class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde):
        # Varmistetaan, ettei yritetä mennä rajojen ulkopuolelle
        if kohde > self.ylin_kerros:
            kohde = self.ylin_kerros
        elif kohde < self.alin_kerros:
            kohde = self.alin_kerros

        # Siirrytään ylöspäin
        while self.nykyinen_kerros < kohde:
            self.kerros_ylos()

        # Siirrytään alaspäin
        while self.nykyinen_kerros > kohde:
            self.kerros_alas()


# Pääohjelma
if __name__ == "__main__":
    # Luodaan hissi, jonka alin kerros on 1 ja ylin 10
    h = Hissi(1, 10)

    print("Siirrytään 5. kerrokseen:")
    h.siirry_kerrokseen(5)

    print("\nPalataan takaisin alimpaan kerrokseen (1. kerros):")
    h.siirry_kerrokseen(h.alin_kerros)