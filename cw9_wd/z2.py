import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
xlsx = pd.ExcelFile('cw9_wd/imiona.xlsx')
df = pd.read_excel(xlsx,'Imie')
df = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = df.plot.bar()
plt.show()