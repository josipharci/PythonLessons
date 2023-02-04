'''
Napišite program u kojem su navedene varijable a=5, b=10, 
c=15, d=21. Program mora vratiti aritmetičku sredinu danih 
brojeva. Rezultat spremite u varijablu jer će se vrijednost koristiti i u 
sljedećem zadatku. Aritmetička sredina računa se tako da se sve 
dane vrijednosti zbroje te se rezultat podijeli s brojem varijabli

'''
a = 5
b = 10
c = 15
d = 21

x = a + b + c + d / 4

# print(x)

'''

iskoristite prethodni zadatak te dobiveni rezultat pretvorite u cijeli broj
i tu vrijednost spremite u varijablu. Nad cjelobrojnom aritmetičkom 
sredinom koju ste prethodno spremili u varijablu napravite
kvadriranje i ispišite dobiveni rezultat

'''
y = int(x) ** 2

print(y)

'''
Korištenjem skraćenih aritmetičkih operatora rezultat dobiven iz 
prethodnog zadatka pomnožite sa 100 i ispišite dobivenu vrijednost.

'''
y*=100

print(y)

'''
Pomoću operatora usporedbe provjerite je li broj koji ste dobili u 
prethodnom zadatku manji od 500. Ispišite rezultat usporedbe (ispis 
će biti vrijednosti "True" ili "False").

'''

print(y < 500)