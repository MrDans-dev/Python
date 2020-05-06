import numpy as np
import pandas as pd
import xlrd
import openpyxl
xlsx = pd.ExcelFile('cw8_wd/imiona.xlsx')
df = pd.read_excel(xlsx,'Imie')
print(df)