'''
Napišite program koji se sastoji od pet varijabli. S jednim pozivom 
funkcije print() ispišite svih pet vrijednosti

'''

var1 = "Auto"
var2 = "BMW"
var3 = "je"
var4 = "super"
var5 = "i dobar!"

print(var1 , var2 , var3 , var4 , var5)

'''
Nastavno na prethodni zadatak, doradite poziv funkcije print()
tako da vrijednost svake pojedine varijable bude u novom redu

'''
print(var1 , var2 , var3 , var4 , var5 , sep='\n')

'''
Napišite program koji ispisuje niz znakova: "Hello World" te neka se 
na kraj ispisanog niza ispiše i znak "!". Uskličnik funkciji print()
prenesite kao end argument.

'''
var = "Hello World"
print(var,end='!')

'''
Napišite program koji se sastoji od dvije varijable. Vrijednosti tih 
varijabli učitajte preko tipkovnice te ih ispišite na zaslon ekrana. 
Prilikom upisivanja vrijednosti u varijable obavijestite korisnika da 
mora unijeti neku vrijednost, npr. "Unesite prvi niz znakova: ". To 
napravite bez korištenja funkcije print().

'''

niz1 = input("Unesite prvi niz znakova:")
niz2 = input("Unesite drugi niz znakova:")

print("-->",niz1,niz2,"<--")

