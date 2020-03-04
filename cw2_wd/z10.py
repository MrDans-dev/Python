n = int(input("Podaj wysokosc: "))
if n < 10:
    for i in range(0, n+1):
        for a in range(0 , i):
             print(f"A",end='')
        print("\n")