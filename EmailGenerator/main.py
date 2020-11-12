import random
e_adress = ['@onet.pl' , '@wp.pl' , '@gmail.com', '@poczta.onet.pl']
e_adress_len = len(e_adress)

def nick():
    nick = input("Nick: ")
    nick = str.lower(nick)
    print(nick+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])
    print()




def name():
    name = input("Name: ")
    l_name = input("Last Name: ")

    name = str.lower(name)
    l_name = str.lower(l_name)
    print(l_name+'.'+name+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])
    print(name+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])
    print(l_name+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])
    print(l_name+name[0]+e_adress[random.randrange(e_adress_len)])
    print(name+str(random.randrange(1900))+e_adress[random.randrange(e_adress_len)])
    print()

def comp():
    name = input("Comp. Name: ")
    name = str.lower(name)
    name+='.pl'
    a = ['biuro@' , 'kontakt@' , 'sekretariat@'];
    for i in range(4):
        print(a[random.randrange(len(a))]+name)
    print()


x=0
while(x!=4):
    print("1.Nick")
    print("2.Name Last Name")
    print("3.Company")
    print("4.Exit")
    print("----------------")
    x = int(input("Option: "))
    print()
    if x == 1:
        nick()
    if x == 2:
        name()
    if x == 3:
        comp()
    

