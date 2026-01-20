
vuosiluku = float(input("Kerro jokin vuosiluku. Ohjelma kertoo onko se karkausvuosi"))
if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print(f"{vuosiluku} on karkausvuosi")
else:
    print(f"{vuosiluku} Ei ole karkausvuosi")
