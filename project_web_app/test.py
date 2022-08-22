# tworzenie klasy
# klasa jest szablonem
class Czlowiek:
    gatunek = "homo sapiens"

    # metoda inicjalizacyjna
    def __init__(self, imie, nazwisko):
        print("Metoda inicjalizacyjna działa !")
        print("Tworzę człowieka o imiu", imie)
        self.imie = imie
        self.nazwisko = nazwisko

    # dodajemy metode, bo funkcja wewnątrz klasy to metoda
    def powiedz_hej(self):
        print("No hej !")


# Tworzę obiekt
# Instancje klasy Człowiek
adam = Czlowiek("Karol", "Kowalski")
ewa = Czlowiek("Iza", "Kowalczyk")

print(adam.gatunek)
print(dir(adam))
adam.powiedz_hej()
ewa.powiedz_hej()
print("Adam ma na imie", adam.imie, "a na nazwisko mam", adam.nazwisko)
