# Yläluokka
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        pass


# Aliluokka: Kirja
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Julkaisun tyyppi: Kirja")
        print(f"Nimi: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")
        print()


# Aliluokka: Lehti
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Julkaisun tyyppi: Lehti")
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")
        print()

# Pääohs
lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti.tulosta_tiedot()
kirja.tulosta_tiedot()