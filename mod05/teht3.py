on_alkuluku = True
jakaja = 2

tutkittava = int(input("Anna tutkittava kokonaisluku: "))
for jakaja in range(2, tutkittava):
    if tutkittava % jakaja == 0:
        on_alkuluku = False

if on_alkuluku == True:
    print("On alkuluku")
else: print("Ei ole alkuluku")
