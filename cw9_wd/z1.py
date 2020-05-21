import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
xlsx = pd.ExcelFile('cw9_wd/imiona.xlsx')
df = pd.read_excel(xlsx,'Imie')
df = df.groupby(['Rok']).agg({'Liczba':['sum']})
df = df.cumsum()
print(df)
df.plot()
plt.show()