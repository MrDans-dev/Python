list_kat = [0 , 30 , 45 , 60 , 90]
import math as m
sin_list = []
cos_list = []
for i in range(len(list_kat)):
    print(list_kat[i])
    sin_list.append(m.sin(list_kat[i]))
    cos_list.append(m.cos(list_kat[i]))

print(sin_list)
print(cos_list)