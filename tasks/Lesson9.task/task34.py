'''
Napišite program koji se sastoji od liste. Elementi liste neka budu 
proizvoljnih vrijednosti. Ispišite samo one elemente koji se nalaze na 
parnom indeksu.

'''
niz = ["Osijek","Zagreb","Split","Zadar","Šibenik","Vukovar"]
par = 0 

for element in niz:
    if par%2 == 0:
        print(element)
    par += 1


'''
Napišite program koji se sastoji od liste. Program s tipkovnice čita
vrijednosti i tako pročitane vrijednosti sprema u listu. Učitavanje 
prekinuti onoga trenutka kada korisnik unese broj 5.

'''

niz_i = []

while True:
    num = input("Unesi broj: ")
    num = int(num)

    if num == 5:
        break
    else:
        niz_i.append(num)

print(niz_i)
    