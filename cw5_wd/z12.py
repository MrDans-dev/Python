#-*- coding: utf-8 -*-
def mies():
    lista = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    for index in range(1,12):
        yield lista[index]
ob = mies()
for i in range(1,12):
    print(next(ob))
