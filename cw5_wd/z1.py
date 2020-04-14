class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj=rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc
    def wyswietl_nazwe(self):
        print(self.rodzaj)
        print(self.dlugosc)
        print(self.szerokosc)

class Ubrania(Material):
    def wyswietl_dane(rozmiar, kolor, dla_kogo):
        print(rozmiar)
        print(kolor)
        print(dla_kogo)

class Sweter(Ubrania):
    def wyswietl_dane(rodzaj_swetra):
        print(rodzaj_swetra)

sweter = Sweter("welniany", 23, 30)
sweter.wyswietl_nazwe()