#Strukture podataka

lista = ["ivan" , "ana" , 55 , 1335.350]

print(lista)

lista2 = ["Ivan","Luka","Nino","Jan","Tin"]

print(lista2[1])
print(lista2[1:3])
print(lista2[:3])
print(lista2[2:])

#Elementi

for element in lista2:
    print(element)

#Dodaj

lista2.append("Josip")

print(lista2)

#Kopriaj

novaLista = lista2.copy()

print(lista2)

#Obriši

lista2.clear()

print(lista2)

#Broj elemenata određene vrijednosti

lista3 = ["Ivan","Luka","Nino","Jan","Tin","Luka"]

print(lista3.count("Luka"))

#Prošitenje liste s elementima druge liste

lista3 = ["Ivan","Luka","Nino","Jan","Tin","Luka"]
newLista = [525 , 220]

newLista.extend(lista3)
print(newLista)

#Traženje elimenata
print(lista3.index("Luka"))

#Dodavanje na odreženo mijesto

lista3.insert(2,"Marko")

print(lista3)

#Uklanjane elementa s neke pozicije
lista3.pop(2)
print(lista3)

#Uklanjanje elementa određene vijednosti
lista3.remove("Luka")
print(lista3)

while "Luka" in lista3:
    lista3.remove("Luka")
print(lista3)

#Promjena redosljeda
brojevi = [ 1 , 2 , 3 , 4 , 5 , 6 , 7]
brojevi.reverse()
print(brojevi)

#Sortiranje
brojevi2 = [3,5,4,8,9,1,7,2,6,0]
brojevi2.sort()
print(brojevi2)





