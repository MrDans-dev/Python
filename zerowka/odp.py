import matplotlib.pyplot as plt 
import numpy as np
y=[20,10,30,10,50]
x1 = np.arange(len(y))
kolory = ['green','aqua','lightblue','darkkhaki','purple']
plt.title('Tytul')

x=['A','B','C','D','E']
y1=[90,70,130,110,130]
kolory1 = ['aqua','skyblue','aqua','yellow','red']
plt.xticks(x1,x)
plt.bar(x,y1,color=kolory1)
plt.bar(x1,y,color=kolory)

plt.show()