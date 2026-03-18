def konversio(gallona):
    return gallona * 3.785

gallonamaara = int(input("Anna jokin gallona määrä, ohjelma muuttaa sen litroiksi: "))

while True:
    konversio(gallonamaara)
    print(konversio(gallonamaara))
    gallonamaara = int(input("Anna jokin gallona määrä, ohjelma muuttaa sen litroiksi: "))
    if gallonamaara < 0:
        print("Gallonamäärä negatiivinen luku")
        break
