import random

class GeneratorDokToz():

    """
    Klasa odpowiada za generowanie danych dokumentu tożsamości w Polsce.
    Została stworzona, tak, aby przechodziła wszystkie walidacje.
    Funkcja oblicz_sume_i_sprawdz_autentycznosc jest swego rodzaju walidacją sprawdzającą,
    czy na pewno wygenerowany numer dokumetu tożsamości jest prawidłowy w świetle weryfikacji.
    """

    def __init__(self, numer_dowodu=None):
        self.numer_dowodu = numer_dowodu

    def oblicz_sume_i_sprawdz_autentycznosc(self):
        liczby_przypisane_literom = {
            "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19,
            "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
            "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
        }
        wagi = [7, 3, 1, 9, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1]

        suma = 0
        for i in range(len(self.numer_dowodu)):
            znak = self.numer_dowodu[i]
            if znak.isalpha():
                suma += liczby_przypisane_literom[znak] * wagi[i]
            elif znak.isdigit():
                suma += int(znak) * wagi[i]

        return suma % 10 == 0


    def generuj_numer_dowodu(self):
        liczby_przypisane_literom = {
            10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J",
            20: "K", 21: "L", 22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S", 29: "T",
            30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z"
        }
        wagi = [7, 3, 1, 9, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1]

        seria = "".join(random.choices(list(liczby_przypisane_literom.values()), k=3))
        numer = "".join(random.choices("0123456789", k=6))

        self.numer_dowodu = seria + numer

        # Obliczanie sumy i sprawdzanie autentyczności
        if self.oblicz_sume_i_sprawdz_autentycznosc():
            return self.numer_dowodu
        else:
            # Jeśli numer nie przechodzi weryfikacji, generuj nowy numer
            return self.generuj_numer_dowodu()
