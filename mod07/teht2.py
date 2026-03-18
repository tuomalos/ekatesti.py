nimet = set()
kysytty = 0
while True:
    if kysytty == "":
        break
    else:
        kysytty = input("Anna nimi: ")
        if kysytty not in nimet:
            nimet.add(kysytty)
            print("Uusi nimi")
        else:
            print("Aiemmin syötetty nimi")

print("Nimet: ")
for n in nimet:
    print(n)