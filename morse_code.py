kod = {
    "A":"• —",
    "B":"— • • •",
    "C":"— • — •",
    "D":"— • •",
    "E":"•",
    "F":"• • — •",
    "G":"— — •",
    "H":"• • • •",
    "I":"• •",
    "J":"• — — —",
    "K":"— • —",
    "L":"• — • •",
    "M":"— —",
    "N":"— •",
    "O":"— — —",
    "P":"• — — •",
    "Q":"— — • —",
    "R":"• — •",
    "S":"• • •",
    "T":"—",
    "U":"• • —",
    "V":"• • • —",
    "W":"• — —",
    "X":"— • • —",
    "Y":"— • — —",
    "Z":"— — • •"
}
s = input()
a = s.replace(" ","")
#slowo = []
#for i in range(0 , len(a[o])):
#    slowo.append(a[i])
#    o=o+1
for i in range(0, len(a)):
    print(kod[a[i].upper()] ,end="")
    print(" ",end='')