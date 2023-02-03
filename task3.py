#Ispišite količnik učitanih 
#brojeva (rezultat dijeljenja učitanih brojeva). U slučaju dijeljenja s 
#nulom, ispišite da to nije ispravno.

a = int(input("input num1: "))
b = int(input("input num2: "))

if a > b > 0:
  x = a / b 
else: 
  x = "Error"

print(x)