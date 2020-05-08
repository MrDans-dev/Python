import numpy as np

def wys(a,b,c):
    print()
    print("A",a)
    print("B",b)
    print("C",c)

a = np.arange(3*4)
print(a)
a= a.reshape(3,4)
b = a.reshape(4,3)
c = a.reshape(2,6)
wys(a,b,c)
a= a.flat
b= b.flat
c= c.flat
wys(a,b,c)