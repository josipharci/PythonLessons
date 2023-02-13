'''
Napišite funkciju koja prima listu. Funkcija vraća boolean vrijednost 
istina ako su svi elementi liste parni brojevi, a boolean vrijednost laž 
ako postoji barem jedan broj koji nije paran.

'''
def  fun(a):
    for i in a:
        if i%2 == 1:
            return False
    return True

a = [2, 4, 6, 8, 9]

if fun(a) == True:
    print("Svi su elementi parni!")
else:
    print("Postoji barem jedan neparan broj!")







'''
Napišite program koji učitava elemente liste s tipkovnice. Učitavanje 
prekinuti onoga trenutka kada korisnik unese broj 5. Nakon što je 
lista učitana, program mora zamijeniti prvi element s posljednjim, 
drugi element s pretposljednjim i tako redom.

'''

array = []

while True:
    num = input("Unesite broj: ")
    num = int(num)

    if num == 5:
        break
    else:
        array.append(num)

print(array)
array.reverse()
print(array)