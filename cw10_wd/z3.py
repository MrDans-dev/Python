import matplotlib.pyplot as plt
import numpy as np

sin = [np.sin(i) for i in range(0,31)]
cos = [np.cos(i) for i in range(0,31)]
plt.plot(sin,label='sin(x)')
plt.plot(cos,label='cos(x)')
plt.show()