import matplotlib.pyplot as plt
import numpy as np
liczby = [1/i for i in range(1,21)]
print(liczby)
plt.axis([0,len(liczby),0,1])
plt.plot(liczby,color='green',marker=">",linestyle='dotted',label="f(x)=1/x")
plt.title("Wykres funkcji f(x) dla x[1,20]")
plt.legend()
plt.xlabel("X")
plt.ylabel("f(x)")
plt.show()