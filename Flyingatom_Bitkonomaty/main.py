from urllib.request import urlopen as op
from bs4 import BeautifulSoup as soup
from operator import itemgetter
import os

def Update():
    conn = op("https://flyingatom.com/bankomaty-bitcoin")
    page = conn.read()
    conn.close()
    city_info = []
    p_soup = soup(page, "html.parser")
    container = p_soup.find_all("tbody")
    table_row = container[0].find_all('tr')
    for i in range(0, len(table_row)):
        city =(table_row[i].find_all("td"))
        city_info.append({"Miasto":city[0].text,"Ulica":city[1].text,"Wartosc":city[3].text,"URL_Mapa":city[4].a['href']})
    city_info = sorted(city_info, key=itemgetter('Miasto'))
    return city_info


def printInfo(lista,miasto=None,index=None,slownik=["Miasto","Ulica","Wartosc","URL_Mapa"]):
    if index != None:
        for o in slownik:
            print(o, ":", lista[index][o])
        print("===========================")
    else:
        for i in range(len(lista)):
            if (miasto == lista[i]["Miasto"]):
                for o in slownik:
                    print(o,":",lista[i][o])
                print("===========================")
            if miasto == None:
                for o in slownik:
                     print(o,":",lista[i][o])
                print("===========================")
    os.system("pause")

def ListaMiast(lista):
    for i in range(len(lista)):
                print(i,":",lista[i]["Miasto"],"\t\t" ,lista[i]['Ulica'])




#2city_info = Update()
#printInfo(city_info,miasto="Warszawa")
#printInfo(city_info,slownik=["Miasto","Wartosc"])
menu=0
while menu != 3:
    print("1. Wszystkie Informacjie o Bitkonomatach FlyingAtom")
    print("2. Informacje o Miescie")
    print("3. Koniec")
    menu = int(input("Wybierz: "))
    if menu == 1:
        city_info=Update()
        printInfo(city_info)
    if menu == 2:
        city_info=Update()
        ListaMiast(city_info)
        index = int(input("Wybierz: "))
        print()
        printInfo(city_info,index=index)