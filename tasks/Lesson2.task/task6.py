#Napišite program koji će u varijable a i b spremiti dva 
#dvoznamenkasta broja. U varijablu a pohranite zadnju znamenku 
#broja koji se nalazi u varijabli b, a u varijablu b pohranite zadnju 
#znamenku broja koja se nalazi u varijabli a. Ispišite sadržaj varijabli a
#i b.
#Napomena: 159%10 = 9, 159%100 = 59


a = int(input("Number1:"))
b = int(input("Number2:"))

if a + b:
    x = str(a) + str(b%10)
else:
    x="Error"
   
if b + a:
    y = str(b) + str(a%10)
else:
    y ="Error"

a = int(x)
b = int(y)

print(a)
print(b)










