import numpy as np

def foo(a):
   vec = np.arange(1,a+1)
   vec = list(reversed(vec))
   diag = np.diag([a for a in vec])
   return diag

print(foo(3))