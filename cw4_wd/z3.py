import sys
with open("dane.txt", "w") as plik:
    for i in range(0,11):
        plik.write(str(i))
with open("dane.txt", "r") as plik:
    for i in plik:
        print(i, end="")