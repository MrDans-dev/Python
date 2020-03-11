def badanie(a):
    if(a>0): return "Rosnąca"
    if(a<0): return "Malejąca"
    if(a==0): return "Stała"
print("Podaj a")
a = int(input())
print(str(badanie(a)))