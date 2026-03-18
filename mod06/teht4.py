def summalasku(lista):
    summa = 0
    for luku in lista:
        summa = summa + luku
    return summa


lista = [1, 2, 3, 4, 5]
print("Esimerkki listan summa on:",summalasku(lista))