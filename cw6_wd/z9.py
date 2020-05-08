import numpy as np
def fibb(n):
    result = [1, 1]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])

    return result

a = np.array(fibb(25)).reshape(5,5)
print(a)

