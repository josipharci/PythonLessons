'''
Napišite program koji najavljuje korištenje funkcija iz modula math te 
izračunajte i ispišite rezultat: 
sin(2) + cos(1)

'''
from math import cos,sin

sum = sin(2) + cos(1)

print(sum)

'''
Pronađite na Internetu u službenoj Python 3 dokumentaciji kako se 
zove funkcija koja se nalazi u modulu math koja se koristi za 
korjenovanje. Preko tipkovnice unesite broj i ispišite njegov korijen. 
Službenu Python 3 dokumentaciju možete pronaći na URL-u: 
https://docs.python.org/3/library/math.html

'''
import math 

num = input("Unesi broj za korjenovanje: ")
rez = math.sqrt(int(num))

print(rez)
'''
Korištenjem konstanti koje su pohranjene u modulu math ispišite 
vrijednost konstante PI.

'''
from math import pi

print(pi)