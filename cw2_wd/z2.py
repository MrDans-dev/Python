import sys
print("Podaj a b")
s = sys.stdin.readline()
licz = s.split(' ')
licz1 = int(licz[0])
licz2 = int(licz[1])
wynik = licz1*licz2
sys.stdout.write(str(wynik))