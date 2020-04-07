class Slowa:
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2

    def wyswietl_wyrazy(self):
        return self.s1, self.s2

    def sprawdz_czy_palindrom(self):
        if(self.s1==self.s1[::-1]):
            return True
        else:
            return False

    def sprawdz_czy_metagram(self):
        diff = 0
        for i in range(len(self.s1)):
            if(self.s1[i] != self.s2[i]):
                diff=diff+1
            if(diff > 1):
                return False
            return True

    def sprawdz_czy_anagramy(self):
        if(sorted(self.s1)== sorted(self.s2)): 
            return True
        else: 
            return False

slowa1 = Slowa("taat","maat")
print(slowa1.wyswietl_wyrazy())
print(slowa1.sprawdz_czy_palindrom())
print(slowa1.sprawdz_czy_metagram())
print(slowa1.sprawdz_czy_anagramy())