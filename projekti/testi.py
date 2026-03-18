import mysql.connector
import random  
import time

# 1. TIETOKANNAN ASETUKSET
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'salasana',
    'database': 'flight_game',
    'autocommit': True
}


def hae_kolme_planeettaa(kursori, nykyinen_icao):
    sql = f"""
        SELECT ident, name 
        FROM airport 
        WHERE type = 'large_airport' AND ident != '{nykyinen_icao}' 
        ORDER BY RAND() 
        LIMIT 3;
    """
    kursori.execute(sql)
    return kursori.fetchall()


def peli():
    try:
        yhteys = mysql.connector.connect(**config)
        kursori = yhteys.cursor()

        # --- PELAAJAN ALOITUSTILANNE ---
        pelaajan_sijainti = 'EFHK'
        flux_polttoaine = 100
        voittomahdollisuus = 0

        print("🚀 TERVETULOA AVARUUSPELIIN! 🚀")
        print("Tehtäväsi on löytää uusi asuttava planeetta ihmiskunnalle.")
        print("-" * 50)


        while True:
            print(f"\n📍 Sijainti: {pelaajan_sijainti}")
            print(f"🔋 Flux-polttoaine: {flux_polttoaine}%")
            print(f"🎯 Voittomahdollisuus: {voittomahdollisuus}%")
            print("-" * 50)

            planeetat = hae_kolme_planeettaa(kursori, pelaajan_sijainti)
            print("Skanneri löysi 3 mahdollista suuntaa:")

            for i, planeetta in enumerate(planeetat, 1):
                print(f"[{i}] Planeetta {planeetta[1]} (Koodi: {planeetta[0]})")

            valinta = input("\nMille planeetalle hypätään? (1, 2, 3): ")

            if valinta in ['1', '2', '3']:
                valittu_indeksi = int(valinta) - 1
                uusi_planeetta = planeetat[valittu_indeksi]

                print(f"\nKäynnistetään hyperhyppy planeetalle {uusi_planeetta[1]}...")
                time.sleep(1)  # Pieni tauko luo jännitystä
                print("Heitetään noppaa kohtalosta... 🎲")
                time.sleep(1)

                # --- NOPANHEITTO JA LOGIIKKA (Teidän suunnitelmanne mukaan) ---
                noppa = random.randint(1, 10)
                print(f"Nopan silmäluvuksi tuli: {noppa}!")

                if noppa <= 3:
                    print("💥 KRIITTINEN TILANNE! Jouduit asteroidivyöhykkeelle.")
                    print("Menetät suuren määrän polttoainetta!")
                    flux_polttoaine -= 40  # Iso rangaistus

                elif noppa <= 7:
                    print("🛸 Matka sujui normaalisti. Menetit keskiverron määrän polttoainetta.")
                    flux_polttoaine -= 10  # Normaali kulutus

                else:  # Nopat 8, 9 ja 10
                    print("✨ LOISTAVA HYPPY! Löysit madonreiän, etkä kuluttanut yhtään polttoainetta!")
                    # Ei vähennetä polttoainetta

                # Päivitetään pelaajan sijainti
                pelaajan_sijainti = uusi_planeetta[0]

                # Nostetaan voittomahdollisuutta jokaisen hypyn jälkeen
                voittomahdollisuus += 20

                # --- VOITON JA HÄVIÖN TARKISTUS ---
                print("-" * 50)

                if flux_polttoaine <= 0:
                    print("💀 FLUX-POLTTOAINE LOPPUI! Avaruusaluksesi jäi ajelehtimaan tyhjyyteen.")
                    print("GAME OVER. Olet hävinnyt pelin.")
                    break  # Tämä komento lopettaa while-luupin ja pelin

                if voittomahdollisuus >= 100 and noppa >= 8:
                    # Teidän vaatimuksen mukaan: "Peli ilmoittaa, että planeetta on asumiskelpoinen..."
                    print("🌍 ONNEKSI OLKOON! Olet saavuttanut uuden galaksin!")
                    print("Planeetta on asumiskelpoinen ja olet löytänyt ihmiskunnalle uuden kodin!")
                    print("VOITIT PELIN! 🎉")
                    break  # Lopettaa pelin voittoon

            else:
                print("\n❌ Virheellinen valinta! Yritä uudelleen.")

    except mysql.connector.Error as virhe:
        print(f"💥 Tietokantavirhe: {virhe}")

    finally:
        if 'yhteys' in locals() and yhteys.is_connected():
            kursori.close()
            yhteys.close()


if __name__ == "__main__":
    peli()