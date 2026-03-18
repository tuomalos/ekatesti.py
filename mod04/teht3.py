luku = input("Anna luku: ")
lukuf = float(luku)
pienin = lukuf
suurin = lukuf


while True:
    luku = input("Anna luku: ")
    if luku == "":
        break

    lukuf = float(luku)
    if lukuf < pienin:
        pienin = lukuf
    if lukuf > suurin:
        suurin = lukuf

print("Pienin luku on", pienin)
print("Suurin luku on", suurin)


