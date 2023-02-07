'''
U varijable a, b, c, d, e spremite pet različitih brojeva. Ako su bar tri 
od pet brojeva veći od 100, tada ispišite poruku "Zadovoljava.", u 
suprotnom ispišite poruku "Ne zadovoljava.".

'''
a = 11
b = 95
c = 888
d = 123
e = 101
counter = 0

if a > 100:
    counter += 1
if b > 100:
    counter += 1
if c > 100:
    counter += 1
if d > 100:
    counter += 1
if e > 100:
    counter += 1

if counter >= 3:
    print("Zadovoljava")
else:
    print("Ne zadovoljava")