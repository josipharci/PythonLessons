'''
. Nadogradite prethodni zadatak tako da ako je korisnik unio manje od 
6 vrijednosti u listu, na primjer korisnik je unio 3 vrijednosti (četvrta 
unesena vrijednost je 5), ostale 3 vrijednosti neka se postave na 
predefiniranu vrijednost, a to je 0.

'''


niz_i = []
cou = 0

while True:
    num = input("Unesi broj: ")
    num = int(num)

    if num == 5:
        break
    else:
        cou += 1
        niz_i.append(num)

while cou < 6:
    niz_i.append(0)
    cou += 1

print(niz_i)


'''
Prethodni zadatak nadogradite tako da nakon završetka upisivanja 
petlja ispiše sve elemente liste zajedno s njihovim pripadajućim 
indeksima. Primjer: 
Unesite broj: 1
Unesite broj: 2
Unesite broj: 3
Unesite broj: 4
Unesite broj: 5
[0] = 1
[1] = 2
[2] = 3
[3] = 4
[4] = 0
[5] = 0
'''

