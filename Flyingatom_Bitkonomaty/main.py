import Bitinfo as info

menu=0
while menu != 3:
    print("1. Wszystkie Informacjie o Bitkonomatach FlyingAtom")
    print("2. Informacje o Miescie")
    print("3. Koniec")
    menu = int(input("Wybierz: "))
    if menu == 1:
        info.printInfo()
    if menu == 2:
        info.ListaMiast()
        index = int(input("Wybierz: "))
        print()
        info.printInfo(index=index)