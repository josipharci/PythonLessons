'''
Napišite funkciju mnozenje() koja može primiti 2 vrijednosti, od 
kojih je druga vrijednost unaprijed zadana, sami odredite broj koji 
ćete pridružiti unaprijed zadanoj vrijednosti. Funkcija mora izračunati 
i ispisati rezultat množenja.

U glavnom dijelu programa pozovite funkciju dva puta. Kod prvog 
poziva funkcije, kao argumente funkcije navedite dvije vrijednosti 
(vrijednost drugog argumenta neka bude drugačija od unaprijed 
zadane vrijednosti). Drugi put funkciju pozovite samo jednim 
argumentom.

'''

def množenje(a,b = 10):
    x = a * b
    print(x)

množenje(int(input("num1:")), 10)
množenje(10)

