'''
Napišite program koji će kreirati praznu tekstualnu datoteku naziva 
datoteka.txt (ako datoteka identičnog imena već postoji od prije, 
tada ju je potrebno pregaziti s praznom datotekom) te je u tako 
kreiranu datoteku potrebno ispisati sve parne brojeve do 20. Parni 
brojevi neka međusobno budu odvojeni razmakom.
'''

with open("datoteka.txt", "w") as f:
    for i in range(0,20):
        if i%2 == 0:
            f.write(str(i) + "")


'''
Izmijenite prethodni zadatak tako da se kreira datoteka naziva 
datoteka.txt. U tako kreiranu datoteku spremite sve brojeve od 1 
do 10. Svaki broj neka bude u zasebnoj liniji. Nakon što je datoteka 
kreirana, pročitajte iz nje sve brojeve te napravite sumu pročitanih 
brojeva, a taj rezultat ispišite na zaslon.

'''

with open("datoteka.txt", "w") as f:
    for i in range(1,11):
            f.write(str(i) + "\n")

suma = 0
with open("datoteka.txt", "r") as f:
    for i in f.readlines():
        suma += int(i)

print(suma)
       
'''
Izmijenite prethodno napisani program tako da se ukupna suma 
brojeva iz datoteke datoteka.txt zapiše na kraj datoteke u 
formatu: "<55>".

'''

with open("datoteka.txt", "w") as f:
    for i in range(1,11):
            f.write(str(i) + "\n")

suma = 0
with open("datoteka.txt", "r") as f:
    for i in f.readlines():
        suma += int(i)

with open("datoteka.txt", "a") as f:
    f.write("<" + str(suma) + ">")
