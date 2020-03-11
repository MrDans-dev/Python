A = []
B = []
C = []
{A.append(i) for i in range(1,11)}
{B.append(pow(2,i)) for i in range(0,10)}
{C.append(B[i]) for i in range(0,len(B))}
print(A)
print(B)
print(C)