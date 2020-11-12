import random
e_adress = ['@onet.pl' , '@wp.pl' , '@gmail.com', '@poczta.onet.pl']
e_adress_len = len(e_adress)

def nick():
    nick = input("Nick: ")
    nick = str.lower(nick)
    print(nick+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])




def name():
    name = input("Name: ")
    l_name = input("Last Name: ")

    name = str.lower(name)
    l_name = str.lower(l_name)
    print(l_name+'.'+name+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])
    print(name+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])
    print(l_name+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])
    print(l_name+name[0]+e_adress[random.randrange(e_adress_len)])


print("1.Nick")
print("2.Name Last Name")
print("----------------")
x = int(input())
if x == 1:
    nick()
else:
    name()

