import numpy as np

def generuj(a,b):
    return np.logspace(1,b,b,True,a,'int')

print(generuj(2,4))
print(generuj(2,5))