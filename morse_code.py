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
    "N":"— •"

}
s = input()
a = s.split(" ")
for i in range(0, len(a)):
    print(kod[a[i].upper()] ,end="")
    print("\t",end='')