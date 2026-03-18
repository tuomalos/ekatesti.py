lentoasematiedot = {}

while True:
    syote= input("Haluatko syöttää uuden lentoaseman tiedot, hakea listasta vai lopettaa uusi/hakea/lopettaa: ")
    if syote == "lopettaa":
        print("Ohjelma lopetettu")
        break
    elif syote == "uusi":
        koodi = input("Anna aseman icao koodi: ")
        kentta = input("Anna aseman nimi: ")
        lentoasematiedot[koodi] = kentta
        print("Asema syötetty")
    elif syote == "hakea":
        icao = input("Anna kentän icao koodi: ")
        if icao in lentoasematiedot:
            print("Lentoasema löydetty")
        else:
            print("Lentoasemaa ei löydetty")
