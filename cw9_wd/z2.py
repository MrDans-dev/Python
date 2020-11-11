import pandas as pd
import matplotlib.pyplot as plt
import xlrd
xlsx = pd.ExcelFile('cw9_wd/imiona.xlsx')
df = pd.read_excel(xlsx,'Imie')
df = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(df)
wykres = df.plot.bar()
plt.show()