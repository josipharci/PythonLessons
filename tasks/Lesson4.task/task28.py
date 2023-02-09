'''
Napišite funkciju koja prima 2 parametara. Rezultat izračuna funkcije 
ovog puta se ne ispisuje izravno u funkciji nego u glavnom dijelu 
programa. Funkcija mora izračunati rezultat formule:
(a*a) + (b*b)
Rezultat spremite u varijablu koja se nalazi u dijelu programskoga
kôda u kojem se funkcija poziva te ispišite tu varijablu.

'''

def fun(a, b):
    return (a*a) + (b*b)

var1 = fun(5,7)
print (var1)

'''
Pozovite funkciju koja ne prima nijedan parametar, ali mora 
izračunati i ispisati zbroj dvaju brojeva. Brojevi neka se dohvate iz 
glavnog dijela programa preko globalnih varijabli.

'''

def sum():
   return a + b

a = 5
b = 9

res = sum()
print(res)

'''
 Prethodni zadatak napišite, a da ne koristite globalne varijable 
(korištenjem parametara funkcije).
'''
def sum(a,b):
    x = a + b
    print(x)

sum(5,9)