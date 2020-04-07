class Ciagi:
    def __init__(self,ciag):
        self.ciag = []

    def pobierz_elementy(self):
        n = int(input("Podaj ilosc elementow ciagu: "))
        for i in range(0,n):
            self.ciag.append(input())

    def pobierz_parametry(self):
        an = input("Podaj pierwsza wartosc ciagu:\n ")
        self.ciag.append(an)
        r = input("Podaj roznice ciagu:\n ")
        n = int(input("Podaj ilosc elementow ciagu: "))
        for i in range(1,n):
            self.ciag.append(int(self.ciag[i-1]) + int(r))

    def wyświetl_dane(self):
        length = len(self.ciag)
        print("Ciag: ")
        for i in range(length):
            print(self.ciag[i])

    def policz_sume(self):
        suma = 0
        length = len(self.ciag)
        for i in range(length):
            suma = suma + int(self.ciag[i])
        return suma

    def policz_elementy(self):
        length = len(self.ciag)
        print("Liczba elementow ciagu: ")
        for i in range(length):
            if(int(self.ciag[0]) == (int(self.ciag[1]) - int(self.ciag[0]))):
                return length

tab = []
ciag1 = Ciagi(tab)
#ciag1.pobierz_elementy()
ciag1.pobierz_parametry()
print(ciag1.wyświetl_dane())
print("Suma elementow ciagu: ")
print(ciag1.policz_sume())
print(ciag1.policz_elementy())