print("Anna kolme satunnais lukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon")
luku1 = input("Anna ensimmäinen luku")
luku2 = input("Anna toinen luku")
luku3 = input("Anna kolmas luku")
luku1float = float(luku1)
luku2float = float(luku2)
luku3float = float(luku3)
print("Lukujen summa on")
summa = luku1float + luku2float + luku3float
print(summa)
print("Lukujen tulo on")
tulo = luku1float * luku2float * luku3float
print(tulo)
print("Lukujen keskiarvo on")
keskiarvo = summa / 3
print(keskiarvo)
