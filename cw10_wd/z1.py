import matplotlib.pyplot as plt
import numpy as np
liczby = [1/i for i in range(1,21)]
print(liczby)
plt.axis([0,1,0,len(liczby)])
plt.plot(liczby)
plt.xlabel("X")
plt.ylabel("f(x)")
plt.show()