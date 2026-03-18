vuodenajat = ("kevät", "kesä", "syksy", "talvi")
(eka, toka, kolmas, neljas) = vuodenajat
kuukausi = int(input("Anna kuukauden numero: "))
if kuukausi == 1 or 2 or 3:
    print(eka)
elif kuukausi == 4 or 5 or 6:
    print(toka)
elif kuukausi == 7 or 8 or 9:
    print(kolmas)
else: print(neljas)


