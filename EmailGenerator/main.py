import random
e_adress = ['@onet.pl' , '@wp.pl' , '@gmail.com']
name = input("Name: ")
l_name = input("Last Name: ")

e_adress_len = len(e_adress)
while(1):
    print(l_name+'.'+name+str(random.randrange(100))+e_adress[random.randrange(e_adress_len)])