#Skup

skup = {1,5,1,5,4,7,8,2,3,2}
print(skup)

#unija

skup1 = {1,5,1,5,4,7,8,2,3,2}
skup2= {1,2,3,6}

print(skup1 | skup2)

# Presjek

print(skup1 & skup2)

#Skupovna razlika
print(skup1 - skup2)
print(skup2 - skup1)

#Komplement presjeka
print(skup1 ^ skup2)


# Riječnik

Hrvatski = { 1 : "Sječanj" , 2:"Veljača",3:"Ožuljak",4:"Travanj",5:"Svibanj",6:"Lipanj",7:"Srpanj",8:"Kolovoz",9:"Rujanj",10:"Listopad",11:"Studeni" ,12:"Prosinac"}

print(Hrvatski[2])
print(Hrvatski[6])

# Dohvačanje ključa

print(Hrvatski.keys())

#Dodavanje novog para 

Hrvatski2 = { 1 : "Sječanj" , 2:"Veljača",3:"Ožuljak",4:"Travanj",5:"Svibanj",6:"Lipanj"}
Hrvatski2.update({7 : "Srpanj"})
print(Hrvatski2.keys())

# Dohvačanje popis vrijednosti

print(Hrvatski2.values())

#Brisanje

del Hrvatski2[1]
del Hrvatski2[2]
print(Hrvatski2)

#Dohvačanje broja elemenata u riječniku

print(len(Hrvatski2))

