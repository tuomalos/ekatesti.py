import random


def noppa(tahkot):
    return random.randint(1,tahkot)


tahkomaara = int(input("Mikä on nopan suurin silmämäärä: "))
heitto = 0
while heitto != tahkomaara:
    heitto = noppa(tahkomaara)
    print(heitto)