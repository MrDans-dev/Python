import numpy as np
a = np.arange(9).reshape(3,3)
b = np.arange(16).reshape(4,4)
a_col = []
a_row = []
b_col = []
b_row = []
print(a)
print()
print(b)
print()
for i in range(3):
    a_col.append(min(a[:,i]))
    a_row.append(min(a[i,:]))
    
for i in range(4):
    b_col.append(min(b[:,i]))
    b_row.append(min(b[i,:]))

print("Min in Column A: ", a_col)
print("Min in Row A: ", a_row)
print()
print("Min in Column B: ", b_col)
print("Min in Row B: ", b_row)