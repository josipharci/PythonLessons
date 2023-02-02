# Zadatak 1:  Kreirajte dijagram toka koji učitava tri broja. Ispišite sumu (a + b + c) 
# ili umnožak unesenih brojeva (a * b * c) ovisno o tome koja je od tih 
# dviju vrijednosti veća.
# Napravi kod za zadatak

# sum vrijednost = 5
# mult vrijednost = 4

a= 1
b= 2
c= 2

sum = a + b + c 
mult = a * b * c 

if sum > mult:
    x = sum
    y = bool(x)
else:
    x = mult
    y = bool(x)

print(x , y)