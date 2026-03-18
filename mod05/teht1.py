import random

kuutiot = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0
for i in range(kuutiot):
    silmaluku = random.randint(1, 6)
    summa += silmaluku
    print(f"Noppa {i + 1}, tulos = {silmaluku}")

print(f"Noppien summa on = {summa}")



