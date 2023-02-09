'''
Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz 
znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od 
unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti 
i ispisati informaciju da je veliko slovo "A" pronađeno.

'''

array = "Abeceda Hrvatska"


counter=0
latA=0

for x in array:
    if x >= "A" and x <= 'Z':
        counter += 1

    if x == "A":
        latA = 1
        print('veliko slovo "A" je pronađeno!')

if latA == 0:
    print(counter)