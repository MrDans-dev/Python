import numpy as np
import pandas as pd

file = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(file,'Imie')
print(data)