'''
U varijable a i b spremite dva broja. Ispišite poruku "Zadovoljava."
ako se barem jedan od brojeva nalazi u intervalu [5, 20], u 
suprotnom ispišite poruku "Ne zadovoljava.".

'''

a = int(input("Num1:"))
b = int(input("Num2:"))


if a >= 5 and a <= 20 or b >= 5 and b <= 20:
    print("Zadovoljava")
else:
    print("Ne zadovoljava")