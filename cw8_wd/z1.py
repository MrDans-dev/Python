import numpy as np
import pandas as pd
import xlrd
import openpyxl
import os
print("PLIKI: ",list(os.listdir()))
print()
xlsx = pd.ExcelFile('cw8_wd/imiona.xlsx')
df = pd.read_excel(xlsx,'Imie')
print(df)