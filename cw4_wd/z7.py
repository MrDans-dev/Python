class Robaczek:
     def __init__(self, x, y, krok):
         self.x = x
         self.y = y
         self.krok = krok

     def idz_w_gore(self,ile_krokow):
        self.y = self.y + ile_krokow * self.krok

     def idz_w_dol(self,ile_krokow):
        self.y = self.y - ile_krokow * self.krok

     def idz_w_lewo(self,ile_krokow):
        self.x = self.x - ile_krokow * self.krok

     def idz_w_prawo(self,ile_krokow):
        self.x = self.x + ile_krokow * self.krok

     def pokaz_gdzie_jestes(self):
        return self.x, self.y

     def test(self):
         return 0

     def __del__(self):
        print("Usuniecie.")

robaczek1 = Robaczek(0,0,1)
robaczek1.idz_w_gore(3)
print(robaczek1.pokaz_gdzie_jestes())
robaczek1.idz_w_lewo(2)
robaczek1.idz_w_dol(8)
print(robaczek1.pokaz_gdzie_jestes())
robaczek1.idz_w_prawo(5)
print(robaczek1.pokaz_gdzie_jestes())

del robaczek1