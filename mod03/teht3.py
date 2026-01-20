sukupuoli = input("Oletko nainen vai mies")
arvo = float(input("Mikä on sinun hemoglobiini arvo"))
if sukupuoli == "nainen":
    if arvo < 117:
        tulos = "alhainen"
    elif arvo > 175:
        tulos = "korkea"
    else: tulos = "normaali"
if sukupuoli == "mies":
    if arvo < 143:
        tulos = "alhainen"
    elif arvo >195:
        tulos = "korkea"
    else: tulos = "normaali"
print(f"Hemoglobiini arvosi on {tulos}")
