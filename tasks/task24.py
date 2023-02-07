'''
U varijable a1, a2, b1, b2 spremite četiri cijela broja. Neka 
vrijednosti koje spremite u varijable zadovoljavaju sljedeće uvjete: a1
< a2 i b1 < b2. Te vrijednosti predstavljaju granice dvaju intervala 
[a1, a2] – prvi interval i [b1, b2] – drugi interval. Provjerite je li drugi 
interval smješten unutar prvog intervala.
Napomena: provjerite je li početna granica prvog intervala manja ili 
jednaka početnoj granici drugog intervala (a1 ≤ b1) te je li završna 
granica prvog intervala veća ili jednaka završnoj granici drugog 
intervala (b2 ≤ a2). 
Ako su ovi uvjeti zadovoljeni, ispišite poruku "Zadovoljava.", u 
suprotnom ispišite poruku "Ne zadovoljava.".

'''
a1 = int(4)
a2 = int(8)

b1 = int(5)
b2 = int(7)

if a1 <= b1 and a2 >= b2:
    print("Zadovoljava")
else: 
    print("Ne zadovoljava")


'''
Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno 
djeljivi i s 5 i s 13.

'''

for n in range(1,1000):
    if n%2 == 0 and n%5 == 0 and n%13 == 0:
        print(n)