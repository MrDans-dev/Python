import pandas as pd
import xlrd
xlsx = pd.ExcelFile('cw8_wd/imiona.xlsx')
df = pd.read_excel(xlsx,'Imie')
print(df[(df["Liczba"]>1000)])
print()
print(df[(df["Imie"] == "DANIEL")])
print()
print(df.groupby(['Rok']).agg({'Liczba':['sum']}))
print()
print(df[(df["Rok"]>=2000)&(df["Rok"]<=2005)].groupby("Rok").agg({'Liczba':['sum']}))
print()
print(df.groupby("Plec").agg({'Liczba':['sum']}))
print()