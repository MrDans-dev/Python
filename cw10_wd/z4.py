import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,30,0.1)
sin = np.sin(x)+2
sin2 = np.sin(x)
plt.plot(sin,label='sin(x)')
plt.plot(sin2,label='sin(x)')
plt.axis([0,30,-1,3])
plt.show()