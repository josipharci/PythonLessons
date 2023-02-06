'''
U varijable a i b spremite dva broja. Ako je vrijednost varijable a bar 
za 50 veća od vrijednosti varijable b, a uz to je vrijednost varijable b
parna, tada ispišite poruku "Uvjeti su zadovoljeni.", u suprotnom 
ispišite poruku "Uvjeti nisu zadovoljeni."

'''

a = int(input("num1:"))
b = int(input("num2:"))

if a > (b + 50) and b % 2 == 0:
    print("Uvijet je ispunjen")
else:
    print("Uvijet nije ispunjen")