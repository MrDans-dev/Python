class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyświetl_produkt(self):
        return self.nazwa_produktu,self.ilosc, self.jednostka_miary, self.cena_jed

    def ile_produktu(self):
        return str(self.ilosc) + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed




zakup1 = NaZakupy("Chleb",10,"kg",0.99)
print(zakup1.wyświetl_produkt())
print(zakup1.ile_produktu())
print(zakup1.ile_kosztuje())