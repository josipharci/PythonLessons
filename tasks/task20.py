'''
U varijable a i b spremite dva broja. Ako je jedan od brojeva veći od 
100, a onaj drugi manji od 100, tada ispišite poruku "Jedna je veća, a 
druga je manja od 100.". Također, ispišite prikladne poruke i za 
slučaj ako su obje vrijednosti veće od 100 ili pak za slučaj ako su 
obje vrijednosti manje od 100 te ako su obje vrijednosti jednake 100

'''
a = int(input("Broj 1:  "))
b = int(input("Broj 2:  "))

if a > 100 and b < 100 or a < 100 and b > 100:
    print("Jedna je veća a druga manja od 100")
elif a > 100 and b > 100:
    print("Obje vrijednosti su veče od 100")
elif a < 100 and b < 100:
    print("Obje Vrijednosti su manje od 100")
else:
    print("Vrijednosti su jednake")
