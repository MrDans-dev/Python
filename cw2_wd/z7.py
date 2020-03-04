a = input()
a = a.split(" ")
liczby = [int(liczba) for liczba in a]
for i in range(0 , len(liczby)):
    print(liczby[i]*liczby[i],end='')
    print(" ",end='')