import sys
plik = open("liczby.txt","w")
for i in range(1,101):
    if i%4==0:
        plik.write(str(i)+"\n")
plik.close()
