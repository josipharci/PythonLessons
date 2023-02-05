'''
Kreirajte dvije varijable i pridružite im neki niz znakova. Isprobajte 
kako funkcioniraju operatori za rad s nizovima znakova (spajanje, 
ponavljanje, dohvaćanje vrijednosti na indeksu, vraćanje dijela niza 
omeđenog indeksima, provjera nalazi li se dani znak u nizu, provjera 
NE nalazi li se dani znak u nizu).

'''

a = "I love @"
b = "Croatian"

x = a + b
print(x)

x = a * 2
print(x)

x = a[0]
print(x)

x = b[0]
print(x)

x = 'c' in a
print(x)

x = 'C' in b
print(x)

x = 'l' not in a
print(x)

x = 'H' not in b
print(x)
