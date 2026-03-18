while True:
    tuuma = float(input("Anna tuuma määrä muutetaan senteiksi: "))
    if tuuma <=0:
        print("Anna positiivinen luku")
        break
    print(f"{tuuma} tuumaa on = {tuuma * 2.54}cm")



