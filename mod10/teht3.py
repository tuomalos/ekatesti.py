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


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        # Luodaan lista, johon lisätään annettun määrän verran Hissi-olioita
        self.hissit = []
        for _ in range(hissien_lukumaara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissia(self, hissin_numero, kohdekerros):
        if 1 <= hissin_numero <= len(self.hissit):
            print(f"\n--- Ajetaan hissiä numero {hissin_numero} kerrokseen {kohdekerros} ---")
            valittu_hissi = self.hissit[hissin_numero - 1]
            valittu_hissi.siirry_kerrokseen(kohdekerros)
        else:
            print(f"Hissiä numero {hissin_numero} ei ole olemassa.")

    def palohalytys(self):
        print("\n" + "=" * 40)
        print("!!! PALOHÄLYTYS !!!")
        print("Kaikki hissit ajetaan pohjakerrokseen!")
        print("=" * 40)
        # Käydään kaikki hissit läpi ja ajetaan ne alimpaan kerrokseen
        for i in range(len(self.hissit)):
            # Hyödynnetään jo olemassa olevaa aja_hissia-metodia
            # Hissien numerointi alkaa ykkösestä, joten annetaan parametreiksi (i + 1) ja self.alin_kerros
            self.aja_hissia(i + 1, self.alin_kerros)


# Pääohjelma
if __name__ == "__main__":
    # Luodaan talo, jossa on alin kerros 1, ylin kerros 7 ja 3 hissiä
    print("Luodaan talo (kerrokset 1-7, 3 hissiä).")
    talo = Talo(1, 7, 3)

    # Ajellaan hisseillä, jotta ne ovat eri kerroksissa
    talo.aja_hissia(1, 5)  # Hissi 1 viidenteen kerrokseen
    talo.aja_hissia(2, 7)  # Hissi 2 ylimpään kerrokseen
    talo.aja_hissia(3, 3)  # Hissi 3 kolmanteen kerrokseen

    # Käynnistetään palohälytys
    talo.palohalytys()