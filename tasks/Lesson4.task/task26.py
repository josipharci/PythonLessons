'''
Napišite funkciju koja ispisuje proizvoljan niz znakova, na primjer 
"Hello World!". U glavnom dijelu programa pozovite napisanu 
funkciju.

'''

def funkcija():
    print("Hello World!")

funkcija()


'''
Napišite funkciju koja prima 4 parametara. Funkcija mora ispisati 
rezultat matematičke formule:
( (a*a) + (b*c) – d ) / 2
U glavnom dijelu programa pozovite napisanu funkciju.

'''

def one():
    a = int(input("num1:"))
    b = int(input("num2:"))
    c = int(input("num3:"))
    d = int(input("num4:"))

    x = ((a * a) + (b * c) - d) / 4
    print(x)  

one()